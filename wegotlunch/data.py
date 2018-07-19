"""
Here we define the data format.

(c) Tadas Krisciunas, 2018.
"""

from . import settings

from collections import namedtuple
import pickle

##############################################################
# ---------------------------------------------------------- #
#                     Main app logic                         #
# ---------------------------------------------------------- #
##############################################################


FoodItem = namedtuple('FoodItem', ['placeName',
                                   'itemName',
                                   'price',
                                   'thumbsUpCount',
                                   'thumbsDownCount'])
"""
The definition of a food item.
"""

def createExampleItems():
    """
    Creates a list of example food items and stores them at the
    data location.

    :return:
    """

    _ = input('Are you sure? This will delete existing items.')

    with open(settings.DATA_LOCATION, 'wb') as f:
        pickle.dump([{
                        'placeName': 'Absolutely Starving',
                        'itemName': 'All items in store',
                        'price': 1000,
                        'thumbsUpCount': 1000,
                        'thumbsDownCount': 0
                     },
                     {
                        'placeName': 'Zopa Breakfast',
                        'itemName': 'All items in store',
                        'price': 0,
                        'thumbsUpCount': 1000,
                        'thumbsDownCount': 0
                     }],
                    f)

def addItem(**kwargs):
    """
    Adds an item to datastore.

    :param kwargs: a list of item attributes. Must contain
                    * placeName
                    * itemName
                    * price
                    * thumbsDownCount
                    * thumbsUpCount
    :return: True on success, False o/w
    """

    keys = kwargs.keys()

    if 'placeName' in keys and \
       'itemName' in keys and \
       'price' in keys and \
       'thumbsUpCount' in keys and \
       'thumbsDownCount' in keys:

        with open(settings.DATA_LOCATION, 'rb') as f:
            items = pickle.load(f)

        items.append(kwargs)

        with open(settings.DATA_LOCATION, 'wb') as f:
            pickle.dump(items, f)

        return True

    else:
        return False