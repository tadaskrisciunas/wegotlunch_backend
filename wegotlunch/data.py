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
        pickle.dump([FoodItem(placeName='Absolutely Starving',
                              itemName='All items in store',
                              price='£1000',
                              thumbsUpCount=1000,
                              thumbsDownCount=0),
                     FoodItem(placeName='Zopa Breakfast in Kitchen',
                              itemName='All items in store',
                              price='£0',
                              thumbsUpCount=1,
                              thumbsDownCount=0)
                     ],
                    f)

def addItem(item):
    """
    Adds an item to datastore.

    :param item: a `FoodItem` instance.
    :return: None
    """
