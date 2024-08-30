import logging
from settings import get_app_settings


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
