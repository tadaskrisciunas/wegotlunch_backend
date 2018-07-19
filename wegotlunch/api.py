"""
REST API root file.

(c) Tadas Krisciunas, 2018.
"""

from . import settings
from . import data

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

class AddItem(Resource):

    def get(self, **kwargs):

        if data.addItem(**kwargs):
            return {'Status': 'Item added'}

        else:
            return {'Status': 'Item not added'}

# Add API resources. Define endpoints.
api.add_resource(ListItems, '/listItems')
api.add_resource(AddItem, '/addItem')