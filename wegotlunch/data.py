"""
Here we define the data format.

(c) Tadas Krisciunas, 2018.
"""

from . import settings

import pickle
import pandas as pd

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

    places = pd.read_csv(settings.DATA_CSV_LOCATION)

    with open(settings.DATA_LOCATION, 'wb') as f:
        pickle.dump({i + 1: dict(row) for i, row in places.fillna(0).iterrows()
                                      if row['placeName'] and row['itemName']},
                    f)

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

    # First, validate items
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

def filter_by(field_to_filter):
    """
    Filter all of the items based on an input field

    :param field_to_filter: The field to filter on. E.g. vegetarian
    :return: List of ids that are remaining. E.g. if field_to_filter is vegetarian, this will be a list of vegetarian item ids
    """
    all_items = getAllItems()
    filtered_ids = []

    for item_id in all_items:
        if all_items[item_id][field_to_filter].upper() == "YES":
            filtered_ids.append(item_id)

    return filtered_ids


def sort_by(sort_key, descending=True):
    all_items = []
    for item_id, item in getAllItems().items():
        item['item_id'] = item_id
        all_items.append(item)

    sorted_items = sorted(all_items, key=sort_key, reverse=descending)
    sorted_ids = [item['item_id'] for item in sorted_items]
    return sorted_ids

