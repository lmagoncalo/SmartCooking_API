from flask import request, json, Response, Blueprint
from ..models.IngredientsModel import RecipesModel, RecipesSchema

recipe_api = Blueprint('Recipes', __name__)
recipe_schema = RecipesSchema()


# add this new method
@recipe_api.route('/', methods=['GET'])
def get_all():
  recipes = RecipesModel.get_all_Recipes()
  ser_recipes = recipe_schema.dump(recipes, many=True).data
  return custom_response(ser_recipes, 200)




@recipe_api.route('/<int:recipe_id>', methods=['GET'])
def get_a_user(recipe_id):
  """
  Get a single user
  """
  recipe = RecipesModel.get_one_Recipe(recipe_id)
  if not recipe:
    return custom_response({'error': 'recipe not found'}, 404)
  
  ser_recipe = recipe_schema.dump(recipe).data
  return custom_response(ser_recipe, 200)


def custom_response(res, status_code):
  """
  Custom Response Function
  """
  return Response(
    mimetype="application/json",
    response=json.dumps(res),
    status=status_code
)