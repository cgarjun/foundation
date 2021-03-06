name = "foundation"

version = "0.0.1"

authors = [
    "arjun.thekkumadathil"
]

description = "Production show environment"

tools = [
    "profile_create",
    "suite_create",
    "show_create",
    "asset_create",
    "config_info",
]

requires = [
    "python-2.7+<3",
    "nlogger-0+<1",
]

def commands():
    env.PYTHONPATH.append("{root}/python")
    env.PATH.append("{root}/bin")
    env.FOUNDATION_CONFIG="{root}/config"
    env.N_SHOW_TEMPLATE_DIR="{root}/templates"
