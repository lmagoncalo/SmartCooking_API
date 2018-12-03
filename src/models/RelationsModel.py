# src/models/IngredientesModel.py
from . import db

from marshmallow import fields, Schema

class RelationsModel(db.Model):
  """
  Blogpost Model
  """

  __tablename__ = 'Relations'


  id_relacao = db.Column(db.Integer, primary_key=True)
  id_recipe = db.Column(db.Integer, db.ForeignKey('Recipes.id'), nullable=False)
  id_ingredient = db.Column(db.Integer, db.ForeignKey('Ingredients.id'), nullable=False)

  def __init__(self, data):
    self.id_recipe = data.get('id_recipe')
    self.id_ingredient = data.get('id_ingredient')



  @staticmethod
  def get_all_relations():
    return RelationsModel.query.all()

  """

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
  """

  def __repr__(self):
    return '<id relation {}>'.format(self.id)


class RelationsSchema(Schema):
  """
  Blogpost Schema
  """
  id_recipe = fields.Int(dump_only=True)
  id_ingredient = fields.Int(dump_only=True)
