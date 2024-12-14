import logging
from pathlib import Path


def create_logger(logger_name: str, log_file: str):
    """
    Creates a logger with INFO level, a file handler, and the specified formats.

    :param logger_name: name of the logger - string.
    :param log_file: name if the file that saves logs - string.
    :return: configured logger instance.
    """
    logger = logging.getLogger(logger_name)  # create custom logger
    logger.setLevel(logging.INFO)  # set level fo INFO

    # set the logs/ folder as default for log files and add the provided name for the file
    logger_path = Path(__file__).resolve().parent.parent.parent / "logs" / log_file

    # create a file handler to save logs in a file
    handler = logging.FileHandler(logger_path)

    # set the format for logs saved in the file
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

    handler.setFormatter(formatter)  # set the desired format for logs in the file

    # add file handler to logger
    if not logger.handlers:  # prevent duplicate handlers if logger is reused
        logger.addHandler(handler)

    return logger
