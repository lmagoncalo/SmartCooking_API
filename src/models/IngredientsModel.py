# src/models/IngredientesModel.py
from . import db

from marshmallow import fields, Schema

class IngredientsModel(db.Model):


  __tablename__ = 'Ingredients'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50), nullable=False)
  #owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

  def __init__(self, data):
    self.name= data.get('name')


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
  
  @staticmethod
  def get_all_ingredients():
    return IngredientsModel.query.all()
  
  @staticmethod
  def get_one_ingredient(id):
    return IngredientsModel.query.get(id)

  def __repr__(self):
    return '<id ingredient {}>'.format(self.id)


class IngredientsSchema(Schema):

  id = fields.Int(dump_only=True)
  name = fields.Str(required=True)
