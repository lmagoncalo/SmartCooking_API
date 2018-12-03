from flask_sqlalchemy import SQLAlchemy

# initialize our db
db = SQLAlchemy()


from .RecipesModel import RecipesModel, RecipesSchema
from .IngredientsModel import IngredientsModel, IngredientsSchema
from .RelationsModel import RelationsModel, RelationsSchema
from .VersionModel import VersionModel, VersionSchema
