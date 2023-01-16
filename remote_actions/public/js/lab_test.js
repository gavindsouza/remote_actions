frappe.ui.form.on('Lab Test', {
    refresh: function(frm) {
        frm.add_custom_button(__('Sync Test Results'), function() {
            frm.call("sync_test_results");
        });
    }
});