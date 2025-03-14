## General methods will be written here except the codes are too long.
## MCDReforged is a necessary dependency, install it with command like `pip install mcdreforged`.
from mcdreforged.api.all import *
from typing import Callable, Any

# Init MCDR interfaces and variables.
psi = ServerInterface.psi()
MCDRLocale = psi.get_mcdr_language()


# Usage: @execute_if(bool | Callable -> bool)
def execute_if(condition: bool | Callable[[], bool]):
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> Any:
            actual_condition = condition() if callable(condition) else condition
            if actual_condition:
                return func(*args, **kwargs)
            return None
        return wrapper
    return decorator

def extract_file(server: PluginServerInterface, file_path, target_path):
    '''
    Extract bundled file to target path from the specified plugin.
    
    :param plugin_name: The name of the plugin containing the bundled file.
    :param file_path: The path of the bundled file.
    :param target_path: The path to extract the file, filename must be included.
    '''
    with server.open_bundled_file(file_path) as file_handler:
        with open(target_path, 'wb') as target_file:
            target_file.write(file_handler.read())

def on_load(server: PluginServerInterface, prev_module):
    load_tip = "MoolingUtils loaded successfully!"
    if MCDRLocale != "en_us":
        load_tip = "木泠的工具包已成功加载！"
    server.logger.info(load_tip)