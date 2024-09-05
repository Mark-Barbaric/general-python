from flask_sqlalchemy import SQLAlchemy
from .model.model_class import Base


db = SQLAlchemy(model_class=Base)
