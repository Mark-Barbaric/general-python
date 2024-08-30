from pydantic_settings import BaseSettings
import functools


class WebscrapeSettings(BaseSettings):
    logger_name: str = "root"
    background_task_iterations: int = 10 ** 8
    main_task_iterations: int = 10


@functools.lru_cache
def get_app_settings() -> WebscrapeSettings:
    settings = WebscrapeSettings()
    return settings
