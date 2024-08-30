import logging
from model import TestModel, FullModel
from helpers import write_json_to_file
from settings import get_app_settings


async def custom_coro():
    """_summary_
    """
    logger = logging.getLogger(get_app_settings().logger_name)
    logger.info('Coroutine is running')
    base_models: list[TestModel] = []
    for i in range(get_app_settings().background_task_iterations):
        if i % 100 == 0:
            logger.info(f"Creating model {i}")

        new_model = TestModel(
            name=f"Name: {i}",
            value=i
        )
        base_models.append(new_model)

    # simulate some long running task
    full_model = FullModel(
        models=base_models
    )
    json_bytes = full_model.model_dump_json()
    logger.info("Writing Model to json")
    write_json_to_file(json_bytes, "test.json")
    logger.info('Coroutine is done')
