import os
import logging
from settings import get_app_settings


def write_json_to_file(json_string: str, file_name: str):
    """_summary_

    Args:
        json_string (str): _description_
        file_name (str): _description_
    """
    logger = logging.getLogger(get_app_settings().logger_name)
    file_path = os.path.join(os.getcwd(), file_name)
    logger.info(f"attempting to write json file to path: {file_path}")
    try:
        with open(file_path, 'w') as f:
            f.write(json_string)
    except FileNotFoundError:
        logger.error(f"file_path: {file_path} not found")
