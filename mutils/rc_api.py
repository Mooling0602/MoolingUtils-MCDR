## This module need MCDR plugin env.
from mcdreforged.api.types import CommandSource, ServerInterface


psi = ServerInterface.psi()

class psiLogger:

    def info(self, message):
        psi.logger.info(message)

    def warning(self, message):
        psi.logger.warning(message)
    
    def error(self, message):
        psi.logger.error(message)

    def critical(self, message):
        psi.logger.critical(message)

    def debug(self, message):
        psi.logger.debug(message)

class srcReply:
    def __call__(self, src: CommandSource, message):
        src.reply(message)

    def log(self, src: CommandSource, message):
        src.reply(message)
        psi.logger.info(f"[-> {src.player}] {message}")


class cmdReply:
    def _send_message(self, src: CommandSource, message: str):
        if src.is_player:
            psi.tell(src.player, message)

    def __call__(self, src: CommandSource, message: str):
        self._send_message(src, message)

    def log(self, src: CommandSource, message: str, logger=psiLogger()):
        self._send_message(src, message)
        if src.is_player:
            try:
                logger.info(f"[-> {src.player}] {message}")
            except Exception:
                psi.logger.warning("Your logger instance is incompatible! Fallbacking to psi logger.")
                psi.logger.info(f"[-> {src.player}] {message}")
        else:
            psi.logger.warning("Command is not from any actual player or fake messages!")