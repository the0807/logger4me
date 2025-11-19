import logging
import os
from logging.handlers import RotatingFileHandler

# ANSI Color Code
LOG_COLORS = {
    "DEBUG": "\033[94m",     # Blue
    "INFO": "\033[92m",      # Green
    "WARNING": "\033[93m",   # Yellow
    "ERROR": "\033[91m",     # RED
    "CRITICAL": "\033[95m",  # Purple
    "RESET": "\033[0m",      # Reset
}

class ColorFormatter(logging.Formatter):
    def format(self, record):
        original_levelname = record.levelname

        padded_levelname = f"{original_levelname:<8}"
        color = LOG_COLORS.get(original_levelname, "")
        reset = LOG_COLORS["RESET"]

        record.levelname = f"{color}{padded_levelname}{reset}"
        formatted = super().format(record)

        record.levelname = original_levelname
        return formatted

def get_logger(level: int = logging.INFO, log_file: str = None, save_color: bool = False):
    logger = logging.getLogger()
    logger.setLevel(level)

    if not logger.handlers:
        datefmt = "%Y-%m-%d %H:%M:%S"

        fmt_color_str = "%(asctime)s | %(levelname)s | %(message)s"

        fmt_plain_str = "%(asctime)s | %(levelname)-8s | %(message)s"

        # Console Handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(ColorFormatter(fmt_color_str, datefmt))
        logger.addHandler(console_handler)

        if not log_file == None:
            os.makedirs(os.path.dirname(log_file), exist_ok=True)

            # File Handler
            file_handler = logging.FileHandler(log_file, mode="w", encoding="utf-8")

            if save_color == False:
                file_handler.setFormatter(logging.Formatter(fmt_plain_str, datefmt))
            else:
                file_handler.setFormatter(ColorFormatter(fmt_color_str, datefmt))

            logger.addHandler(file_handler)

    return logger