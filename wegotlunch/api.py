"""
REST API root file.

(c) Tadas Krisciunas, 2018.
"""

from . import settings

from flask import Flask
from flask_restful import Resource, Api
import pickle

##############################################################
# ---------------------------------------------------------- #
#                     Main app logic                         #
# ---------------------------------------------------------- #
##############################################################

app = Flask(__name__)
api = Api(app)

class ListItems(Resource):

    def get(self):

        with open(settings.DATA_LOCATION, 'rb') as f:
            return pickle.load(f)


# Add API resources. Define endpoints.
api.add_resource(ListItems, '/listItems')