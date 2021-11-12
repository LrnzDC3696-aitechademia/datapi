from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from resources.people import People
from resources.sections import Sections
from resources.students import Students

import os


# Must have something in LOCAL (.env) for testing
IS_LOCAL = True if os.getenv('LOCAL') is not None else False

if DATABASE_URI := os.getenv('DATABASE') is None:
    DATABASE_URI = 'sqlite:///database.db'


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI


api = Api(app)
db = SQLAlchemy(app)


def add_resource(api):
    api.add_resource(People)
    api.add_resource(Students)
    api.add_resource(Sections)


add_resource(api)
# db.create_all()


if __name__ == '__main__':
    app.run(debug=IS_LOCAL)

