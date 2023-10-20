import sys
import logging

FORMATTER = logging.Formatter('%(levelname)s - %(asctime)s - %(name)s -  %(message)s')

def init_logger(logger_name: str):
    logger = logging.getLogger("eggs")
    logger.setLevel(logging.INFO)

    return logger

def init_stdout_logger(logger_name: str):
    logger = init_logger(logger_name)
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(FORMATTER)
    handler.setLevel(logging.INFO)
    logger.addHandler(handler)

    return logger

STDOUT_LOGGER = init_stdout_logger('eggs')