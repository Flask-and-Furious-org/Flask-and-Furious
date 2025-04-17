from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from .user import User            
from .ingredient import Ingredient
from .recipe import Recipe, recipe_ingredients
