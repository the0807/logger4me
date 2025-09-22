from logger4me import get_logger

logger = get_logger(
    level = 10, 
    log_file = './logs/app.log', 
    save_color = False
)

logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")
