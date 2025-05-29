from loguru import logger

def setup_logger():
    logger.add("stdout", level="INFO")
