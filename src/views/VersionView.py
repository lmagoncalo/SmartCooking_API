from flask import request, json, Response, Blueprint
from ..models.VersionModel import VersionModel, VersionSchema

version_api = Blueprint('Version', __name__)
version_schema = VersionSchema()


# add this new method
@version_api.route('/', methods=['GET'])
def get_all():
  version= VersionModel.get_version()
  ser_version = version_schema.dump(version).data
  return custom_response(ser_version, 200)





def custom_response(res, status_code):
  """
  Custom Response Function
  """
  return Response(
    mimetype="application/json",
    response=json.dumps(res),
    status=status_code
)