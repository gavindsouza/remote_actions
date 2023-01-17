from io import StringIO
from typing import Dict, List, Optional, Tuple, Union

import frappe
from frappe import _
from frappe.core.utils import find
from frappe.desk.form.save import send_updated_docs
from frappe.utils import now

try:
    from healthcare.healthcare.doctype.lab_test.lab_test import LabTest
except ImportError:
    from erpnext.healthcare.doctype.lab_test.lab_test import LabTest

from xml.etree import ElementTree


class RemoteConnectionNotSetError(frappe.ValidationError):
    ...


class RemoteConnection:
    def __init__(self, *, as_dict=True):
        self.cursor = self.connection.cursor(as_dict=as_dict)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.cursor.close()
        self.connection.close()

    @property
    def connection(self):
        if not hasattr(self, "_connection"):
            self._connection = self.get_remote_connection()
        return self._connection

    def sql(self, sql: str, values: Optional[Union[Dict, Tuple]] = None):
        if values is None:
            values = {}
        self.cursor.execute(sql, values)
        return self.cursor.fetchall()

    def get_remote_connection(self):
        if not frappe.conf.sql_server_connection:
            frappe.throw(_("Remote database not set"), exc=RemoteConnectionNotSetError)
        conn_details = frappe.conf.sql_server_connection
        import pymssql

        return pymssql.connect(
            conn_details["server"],
            conn_details["user"],
            conn_details["password"],
            conn_details["database"],
        )


class CustomLabTest(LabTest):
    REMOTE_VIEW_SQL = """
    SELECT
        dbo.view_analyte.analyte_name,
        dbo.view_analyte_result.result AS analyte_result
    FROM
        dbo.view_patient_test_order
        INNER JOIN dbo.view_analyte_result
            ON dbo.view_patient_test_order.test_ID = dbo.view_analyte_result.test_ID
        INNER JOIN dbo.view_test
            ON dbo.view_analyte_result.test_ID = dbo.view_test.test_ID
        INNER JOIN dbo.view_analyte
            ON dbo.view_analyte_result.analyte_id = dbo.view_analyte.analyte_id
        INNER JOIN dbo.view_patient
            ON dbo.view_patient_test_order.patient_id = dbo.view_patient.patient_id
    WHERE
        dbo.view_patient.gx_patient_id = %(patient_id)s
    """

    @frappe.whitelist()
    def sync_test_results(self):
        patient_barcode = frappe.db.get_value("Patient", self.patient, "barcode")
        if not patient_barcode:
            frappe.throw(_("Patient barcode not set"))

        patient_id = get_id_from_barcode(barcode=patient_barcode)
        if not patient_id:
            frappe.throw(_("Patient ID not found from barcode"))

        remote_values = self.fetch_patient_tests_details(patient_id=patient_id)
        self.update_from_remote_values(remote_values)

        self.save()
        self.add_comment("Comment", f"Test results synced at {now()}")
        frappe.msgprint(_("Test results synced"), alert=True)
        send_updated_docs(self)

    def update_from_remote_values(self, remote_values: List[Dict]):
        for normal_test_item in self.normal_test_items:
            result_value = find(
                remote_values, lambda x: x["analyte_name"] == normal_test_item.lab_test_name
            )
            if result_value:
                normal_test_item.result_value = result_value["analyte_result"]

    def fetch_patient_tests_details(self, patient_id: str) -> List[Dict]:
        with RemoteConnection() as remote:
            return remote.sql(self.REMOTE_VIEW_SQL, {"patient_id": patient_id})


def get_id_from_barcode(barcode: str) -> str:
    return ElementTree.parse(StringIO(barcode)).getroot().get("data-barcode-value")
