#src/app.py

from flask import Flask

from .config import app_config
from .models import db

from .models.IngredientsModel import IngredientsModel


# importa a blueprint
from .views.RecipesView import recipe_api as recipes_blueprint
from .views.IngredientsView import ingredients_api as ingredients_blueprint
from .views.RelationsView import relations_api as relations_blueprint
from .views.VersionView import version_api as version_blueprint



def create_app(env_name):
  """
  Create app
  """
  
  # app initiliazation
  application = Flask(__name__)

  # app.run(host='0.0.0.0',port=5000)

  application.config.from_object(app_config[env_name])


  db.init_app(application) # add this line

  #regista a blueprint
  #testar get por exemplo: http://127.0.0.1:5000/api/recipes/  -->todas as recipes
  application.register_blueprint(recipes_blueprint, url_prefix='/api/recipes')
  application.register_blueprint(ingredients_blueprint, url_prefix='/api/ingredients')
  application.register_blueprint(relations_blueprint, url_prefix='/api/relations')
  application.register_blueprint(version_blueprint, url_prefix='/api/version')


  

  @application.route('/', methods=['GET'])
  def index():
    """
    example endpoint
    """

    return 'Congratulations! Your first endpoint is workin'

  


  return application