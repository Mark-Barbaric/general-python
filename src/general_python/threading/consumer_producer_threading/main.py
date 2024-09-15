import logging
import threading
import time
from concurrent import futures
import random
from logging_config import setup_custom_logger
from settings import get_app_settings
from pipeline import Pipeline


def consumer(pipeline, event):
    """Pretend we're saving a number in the database."""
    logger = logging.getLogger(get_app_settings().logger_name)
    while not event.is_set() or not pipeline.empty():
        message = pipeline.get_message("Consumer")
        logger.info(
            "Consumer storing message: %s  (queue size=%s)",
            message,
            pipeline.qsize(),
        )

    logger.info("Consumer received EXIT event. Exiting")


def producer(pipeline, event):
    """Pretend we're getting a number from the network."""
    logger = logging.getLogger(get_app_settings().logger_name)
    while not event.is_set():
        message = random.randint(1, 101)
        logger.info("Producer got message: %s", message)
        pipeline.set_message(message, "Producer")

    logger.info("Producer received EXIT event. Exiting")


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
