# src/models/VersionModel.py
from . import db

from marshmallow import fields, Schema

class VersionModel(db.Model):


  __tablename__ = 'Version'

  id = db.Column(db.Integer, primary_key=True)
  version = db.Column(db.Integer)

  def __init__(self, data):
    self.version= data.get('version')


  def save(self):
    db.session.add(self)
    db.session.commit()

  def update(self, data):
    for key, item in data.items():
      setattr(self, key, item)
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    de.session.commit()
  

  """
  @staticmethod
  def get_version(value):
      return VersionModel.query.filter_by(version=value).first()
  """


  #get last version
  @staticmethod
  def get_version():
    return VersionModel.query.order_by('id').first()

  def __repr__(self):
    return '<version: {}, id:{}>'.format(self.version, self.id)


class VersionSchema(Schema):

  id = fields.Int(dump_only=True)
  version = fields.Str(required=True)
