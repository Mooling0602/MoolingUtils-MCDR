from mcdreforged.api.all import *


def on_load(server: PluginServerInterface, prev_module):
# Init MCDR variables.
    MCDRLocale = server.get_mcdr_language()
    load_tip = "MoolingUtils loaded successfully!"
    if MCDRLocale != "en_us":
        load_tip = "木泠的工具包已成功加载！"
    server.logger.info(load_tip)