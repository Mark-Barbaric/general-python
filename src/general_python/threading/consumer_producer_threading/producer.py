import random
import logging
from settings import get_app_settings


def producer(pipeline, event):
    """Pretend we're getting a number from the network."""
    logger = logging.getLogger(get_app_settings().logger_name)
    while not event.is_set():
        message = random.randint(1, 101)
        logger.info("Producer got message: %s", message)
        pipeline.set_message(message, "Producer")

    logger.info("Producer received EXIT event. Exiting")
