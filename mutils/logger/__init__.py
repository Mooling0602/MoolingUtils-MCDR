import datetime

from typing import Optional
from enum import Enum
from mcdreforged.api.rtext import *
from .text import pattern, mc_to_ansi


class LogLevel(Enum):
    DEBUG = 10
    INFO = 20
    WARNING = 30
    ERROR = 40
    CRITICAL = 50

class SimpleLogger:
    def __init__(self, 
            level: LogLevel=LogLevel.INFO,
            log_format: str = "[{prefix}] [{timestamp} {level}] {message}",
            prefix: str = "SimpleLogger"):
        self.level = level
        self.log_format = log_format
        self.prefix = prefix
        self.colors = {
            LogLevel.DEBUG: RColor.dark_blue,
            LogLevel.INFO: RColor.green,
            LogLevel.WARNING: RColorRGB.from_rgb(255, 165, 0),
            LogLevel.ERROR: RColor.red,
            LogLevel.CRITICAL: RColor.dark_red,
            "RESET": RColor.reset
        }

    def log(self, level: LogLevel, message: str, module: Optional[str]=None):
        if level.value >= self.level.value:
            timestamp = datetime.datetime.now().strftime("%H:%M:%S")
            color = self.colors.get(level, self.colors["RESET"])
            colored_level = RText(level.name, color).to_colored_text()
            if pattern.search(message):
                message = mc_to_ansi(message)
            log_output: str = self.log_format.format(
                prefix=self.prefix if module is None else f"{self.prefix} - {module}",
                timestamp=timestamp,
                level=colored_level,
                message=message
            )
            print(log_output)

    def debug(self, message, module: Optional[str]=None):
        self.log(LogLevel.DEBUG, message, module)

    def info(self, message, module: Optional[str]=None):
        self.log(LogLevel.INFO, message, module)

    def warning(self, message, module: Optional[str]=None):
        self.log(LogLevel.WARNING, message, module)

    def error(self, message, module: Optional[str]=None):
        self.log(LogLevel.ERROR, message, module)

    def critical(self, message, module: Optional[str]=None):
        self.log(LogLevel.CRITICAL, message, module)

custom_logger = SimpleLogger()