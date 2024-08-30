import asyncio
import logging
from settings import get_app_settings
from logger import setup_custom_logger
from background_task import custom_coro


async def main():
    logger = logging.getLogger(get_app_settings().logger_name)
    logger.info("launching main thread")
    coro = custom_coro()
    _ = asyncio.create_task(coro)
    await asyncio.sleep(0)

    for _ in range(get_app_settings().main_task_iterations):
        logger.info("sleeping for 2 secs")
        await asyncio.sleep(2)


if __name__ == "__main__":
    logger = setup_custom_logger(get_app_settings().logger_name)
    asyncio.run(main())
