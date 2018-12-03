# src/models/RecipeModel.py
from marshmallow import fields, Schema
from . import db

#from .IngredienteModel import ingredientSchema

class RecipesModel(db.Model):
  """
  User Model
  """

  # table name
  __tablename__ = 'Recipes'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  difficulty = db.Column(db.Integer)
  time = db.Column(db.Integer)
  category = db.Column(db.String(20))
  supplier = db.Column(db.String(50))
  preparation = db.Column(db.String(1500))
  image = db.Column(db.String(200))
  ingredients = db.Column(db.String(500))
  favorite = db.Column(db.Boolean)
  hash = db.Column(db.Text)

  #relacao = relationship("RelationsModelo", uselist=False, backref="Recipes")
  #blogposts = db.relationship('BlogpostModel', backref='users', lazy=True)

  # class constructor
  def __init__(self, data):
    """
    Class constructor
    """
    self.name = data.get('name')
    self.difficulty = data.get('difficulty')
    self.time = data.get('time')
    self.category = data.get('category')
    self.supplier = data.get('supplier')
    self.preparation = data.get('preparation')
    self.image = data.get('image')
    self.ingredients = data.get('ingredients')
    self.favorite = data.get('favorite')
    self.hash = data.get('hash')

  def save(self):
    db.session.add(self)
    db.session.commit()

  def update(self, data):
    for key, item in data.items():
      setattr(self, key, item)
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()


  @staticmethod
  def get_all_recipes():
    return RecipesModel.query.all()

  @staticmethod
  def get_one_recipe(id):
    return RecipesModel.query.get(id)

  """
  @staticmethod
  def get_user_by_email(value):
    return UserModel.query.filter_by(email=value).first()
  """
  
  def __repr(self):
    return '<id recipe {}>'.format(self.id)



# add this class
class RecipesSchema(Schema):
  """
  User Schema
  """
  id = fields.Int(dump_only=True)
  name = fields.Str(required=True)
  difficulty = fields.Int(required=True)
  time = fields.Int(required=True)
  category = fields.Str(required=True)
  supplier = fields.Str(required=True)
  preparation = fields.Str(required=True)
  image= fields.Str(required=True)
  ingredients = fields.Str(required=True)
  favorite = fields.Str(required=True)
  hash = fields.Str(required=True)
  #blogposts = fields.Nested(BlogpostSchema, many=True)