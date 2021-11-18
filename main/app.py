import os

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from .resources.people import People
from .resources.sections import Sections
from .resources.students import Students


if DATABASE_URI := os.getenv('DATABASE') is None:
    DATABASE_URI = 'sqlite:///database.db'

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI

api = Api(app)
db = SQLAlchemy(app)


def create_db(db):
    from main.models import Person, Section, Student
    db.create_all()

def add_resource(api):
    api.add_resource(People)
    api.add_resource(Students)
    api.add_resource(Sections)


add_resource(api)
create_db(db)

