import queue
import logging
from settings import get_app_settings


class Pipeline(queue.Queue):
    def __init__(self):
        super().__init__(maxsize=10)

    def get_message(self, name):
        logger = logging.getLogger(get_app_settings().logger_name)
        logger.debug(name)
        value = self.get()
        logger.debug(f"{name}: got {value} from queue")
        return value

    def set_message(self, value, name):
        logger = logging.getLogger(get_app_settings().logger_name)
        logger.debug(f"{name}: is about to add {value} to queue")
        self.put(value)
        logger.debug(f"{name}: was added {value} to queue")
