"""
REST API root file.

(c) Tadas Krisciunas, 2018.
"""

from . import settings
from . import data

from flask import Flask
from flask_cors import CORS
from flask_restful import Resource, Api, request

##############################################################
# ---------------------------------------------------------- #
#                     Main app logic                         #
# ---------------------------------------------------------- #
##############################################################

app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

def test():
    data.filter_by("vegetarian")

class ListItems(Resource):

    def get(self):
        return {'allItems': data.getAllItems(),
                'itemsById': list(data.getAllItems().keys()),
                'itemsByRating': data.sort_by(lambda item: item['thumbsUpCount'] - item['thumbsDownCount']),
                'itemsByPrice': data.sort_by(lambda item: item['price']),
                'itemsByVegetarian': data.filter_by('vegetarian'),
                'itemsBySeating': data.filter_by('seating')}

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