"""
REST API root file.

(c) Tadas Krisciunas, 2018.
"""

from . import settings
from . import data

from flask import Flask
from flask_restful import Resource, Api, request

##############################################################
# ---------------------------------------------------------- #
#                     Main app logic                         #
# ---------------------------------------------------------- #
##############################################################

app = Flask(__name__)
api = Api(app)

class ListItems(Resource):

    def get(self):
        return data.getAllItems()

class AddItem(Resource):

    def get(self):
        args = {arg: val for arg, val in request.args.items()}

        if data.addItem(**args):
            return {'Status': 'Item added'}

        else:
            return {'Status': 'Item not added'}

class ButtonUpdate(Resource):

    def get(self):
        args = {arg: val for arg, val in request.args.items()}

        if args['thumbs'] == 'true':
            success = data.increaseItemThumbs(int(args['id']), 'thumbsUpCount')

        else:
            success = data.increaseItemThumbs(int(args['id']), 'thumbsDownCount')

        if success:
            return {'Status': 'Item updated'}

        else:
            return {'Status': 'Item not updated'}


# Add API resources. Define endpoints.
api.add_resource(ListItems, '/listItems')
api.add_resource(AddItem, '/addItem')
api.add_resource(ButtonUpdate, '/updateThumbs')