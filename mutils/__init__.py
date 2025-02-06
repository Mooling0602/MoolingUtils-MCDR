from mcdreforged.api.all import *
from typing import Callable, Any


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

def on_load(server: PluginServerInterface, prev_module):
# Init MCDR variables.
    MCDRLocale = server.get_mcdr_language()
    load_tip = "MoolingUtils loaded successfully!"
    if MCDRLocale != "en_us":
        load_tip = "木泠的工具包已成功加载！"
    server.logger.info(load_tip)