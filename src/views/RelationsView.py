from flask import request, json, Response, Blueprint
from ..models.RelationsModel import RelationsModel, RelationsSchema

relations_api = Blueprint('Relations', __name__)
relations_schema = RelationsSchema()


# add this new method
@relations_api.route('/', methods=['GET'])
def get_all():
  relations = RelationsModel.get_all_relations()
  ser_relations = relations_schema.dump(relations, many=True).data
  return custom_response(ser_relations, 200)





def custom_response(res, status_code):
  """
  Custom Response Function
  """
  return Response(
    mimetype="application/json",
    response=json.dumps(res),
    status=status_code
)