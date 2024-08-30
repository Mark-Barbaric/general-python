import logging
import threading
import time
from concurrent import futures
from logging_config import setup_custom_logger
from settings import get_app_settings
from consumer import consumer
from producer import producer
from pipeline import Pipeline


if __name__ == "__main__":
    setup_custom_logger(get_app_settings().logger_name)
    logger = logging.getLogger(get_app_settings().logger_name)
    logger.info("starting main thread")
    pipeline = Pipeline()
    event = threading.Event()

    with futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)
        logger.info("main thread is sleeping for 1 sec")
        time.sleep(0.1)
        logger.info("main thread setting threading.Event")
        event.set()
