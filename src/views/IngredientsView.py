from flask import request, json, Response, Blueprint
from ..models.IngredientsModel import IngredientsModel, IngredientsSchema

ingredients_api = Blueprint('Ingredients', __name__)
ingredients_schema = IngredientsSchema()


# add this new method
@ingredients_api.route('/', methods=['GET'])
def get_all():
  ingredients = IngredientsModel.get_all_ingredients()
  ser_ingredients = ingredients_schema.dump(ingredients, many=True).data
  return custom_response(ser_ingredients, 200)



def custom_response(res, status_code):
  """
  Custom Response Function
  """
  return Response(
    mimetype="application/json",
    response=json.dumps(res),
    status=status_code
)