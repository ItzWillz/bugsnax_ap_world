"""
Items.py - item table.
"""
from typing import NamedTuple
from BaseClasses import ItemClassification

BASE_ID = 3874000

class ItemData(NamedTuple):
    code: int
    classification: ItemClassification
    count: int

item_table: dict[str, ItemData] = {
    'Sauce Slinger': ItemData(BASE_ID + 0, ItemClassification.progression, 1),
    'Buggy Ball': ItemData(BASE_ID + 2, ItemClassification.progression, 1),
    'Lunchpad': ItemData(BASE_ID + 3, ItemClassification.progression, 1),
    'SnakGrappler': ItemData(BASE_ID + 4, ItemClassification.progression, 1),
    'Trip Shot': ItemData(BASE_ID + 5, ItemClassification.progression, 1),
    'Golden Snax': ItemData(BASE_ID + 8, ItemClassification.progression, 50),
    'Story Complete Token': ItemData(BASE_ID + 9, ItemClassification.progression, 1),
    'BUNGER!': ItemData(BASE_ID + 10, ItemClassification.filler, 11),
    'BOPSICLE!': ItemData(BASE_ID + 11, ItemClassification.filler, 11),
    'STRABBY!': ItemData(BASE_ID + 12, ItemClassification.filler, 11),
    'CRAPPLE!': ItemData(BASE_ID + 13, ItemClassification.filler, 11),
    'Ketchup!': ItemData(BASE_ID + 14, ItemClassification.filler, 12),
    'Chocolate!': ItemData(BASE_ID + 15, ItemClassification.filler, 11),
    'Hot Sauce!': ItemData(BASE_ID + 16, ItemClassification.filler, 12),
    'Ranch!': ItemData(BASE_ID + 17, ItemClassification.filler, 11),
    'Peanut Butter!': ItemData(BASE_ID + 18, ItemClassification.filler, 11),
    'Cheese Sauce!': ItemData(BASE_ID + 19, ItemClassification.filler, 11),
}

FILLER_ITEM_NAMES = ['BUNGER!', 'BOPSICLE!', 'STRABBY!', 'CRAPPLE!', 'Ketchup!', "Chocolate!", "Hot Sauce!", "Ranch!", "Peanut Butter!", "Cheese Sauce!"]
MAX_GOLDEN_SNAX = 50
