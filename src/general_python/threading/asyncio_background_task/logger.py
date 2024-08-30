import logging


def setup_custom_logger(logger_name: str):
    """_summary_

    Args:
        name (str): _description_

    Returns:
        _type_: _description_
    """
    formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(module)s - %(message)s')
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    return logger
