import os

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy, event

from .resources.people import People
from .resources.sections import Sections
from .resources.students import Students


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')

api = Api(app)
db = SQLAlchemy(app)
db.create_all()

def add_resource(api):
    api.add_resource(People)
    api.add_resource(Students)
    api.add_resource(Sections)

add_resource(api)

