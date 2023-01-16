from . import __version__ as app_version  # noqa

app_name = "remote_actions"
app_title = "Remote Actions"
app_publisher = "Gavin D'souza"
app_description = "Fetch Data from Remote Databases"
app_email = "gavin18d@gmail.com"
app_license = "Unlicensed"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/remote_actions/css/remote_actions.css"
# app_include_js = "/assets/remote_actions/js/remote_actions.js"

# include js, css files in header of web template
# web_include_css = "/assets/remote_actions/css/remote_actions.css"
# web_include_js = "/assets/remote_actions/js/remote_actions.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "remote_actions/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "remote_actions.utils.jinja_methods",
# 	"filters": "remote_actions.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "remote_actions.install.before_install"
# after_install = "remote_actions.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "remote_actions.uninstall.before_uninstall"
# after_uninstall = "remote_actions.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "remote_actions.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

override_doctype_class = {"Lab Test": "remote_actions.overrides.CustomLabTest"}

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"remote_actions.tasks.all"
# 	],
# 	"daily": [
# 		"remote_actions.tasks.daily"
# 	],
# 	"hourly": [
# 		"remote_actions.tasks.hourly"
# 	],
# 	"weekly": [
# 		"remote_actions.tasks.weekly"
# 	],
# 	"monthly": [
# 		"remote_actions.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "remote_actions.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "remote_actions.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "remote_actions.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]


# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"remote_actions.auth.validate"
# ]
