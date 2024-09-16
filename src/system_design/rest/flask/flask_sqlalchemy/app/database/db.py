from flask_sqlalchemy import SQLAlchemy
from ..domain.model_class import Base


# def _engine_from_url(url: str) -> sa.Engine:
#     logger.debug(f"Making engine from url {url}")
#     # TODO: Make a config flag for SQL Debugging
#     return sa.create_engine(url, echo=False)  # type: ignore[arg-type]

db = SQLAlchemy(model_class=Base)