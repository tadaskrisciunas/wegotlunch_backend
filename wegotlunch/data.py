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


def createExampleItems():
    """
    Creates a list of example food items and stores them at the
    data location.

    :return:
    """

    _ = input('Are you sure? This will delete existing items.')

    with open(settings.DATA_LOCATION, 'wb') as f:
        pickle.dump({
                       1: {
                            'placeName': 'Absolutely Starving',
                            'itemName': 'All items in store',
                            'price': 1000,
                            'thumbsUpCount': 1000,
                            'thumbsDownCount': 0,
                            'picture': 'none',
                            'seating': 1,
                            'address': 'Good address',
                            'vegetarian': True
                          },
                       2: {
                            'placeName': 'Zopa Breakfast',
                            'itemName': 'All items in store',
                            'price': 0,
                            'thumbsUpCount': 1000,
                            'thumbsDownCount': 0,
                            'picture': 'none',
                            'seating': 1,
                            'address': 'Good address',
                            'vegetarian': True
                          }
                    }, f)

def getAllItems():
    """
    Gets all items.
    :return:
    """

    with open(settings.DATA_LOCATION, 'rb') as f:
        return pickle.load(f)

def overwriteAllItems(items: dict):
    """
    Overwrites all items.

    :param items: the new item dictionary to save.
    :return:
    """

    with open(settings.DATA_LOCATION, 'wb') as f:
        pickle.dump(items, f)

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

    # First, validate item
    if 'placeName' in keys and \
       'itemName' in keys and \
       'price' in keys and \
       'thumbsUpCount' in keys and \
       'thumbsDownCount' in keys and \
       'picture' in keys and \
       'seating' in keys and \
       'address' in keys and \
       'vegetarian' in keys:

        items = getAllItems()
        items.update({len(items) + 1: kwargs})
        overwriteAllItems(items)

        return True

    else:
        return False

def increaseItemThumbs(itemId: int,
                       thumbsType: str):
    """
    Increases item's thumbs count by one.

    :param itemId: the id of the item.
    :param thumbsType: either `thumbsUpCount` or `thumbsDownCount`
    :return: True on success, False on failure
    """

    items = getAllItems()

    if itemId in items.keys():
        items[itemId][thumbsType] += 1
        overwriteAllItems(items)
        return True

    else:
        return False