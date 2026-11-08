"""
item_name_translation.py

"""

# apworld item name -> bugsnax_memory internal name (tools use _Selectable pattern)
GRANTABLE_TOOLS = {
    "Buggy Ball": "StrabbyBall",
    "Snak Trap": "SnapTrap",
    "SnakGrappler": "Hookshot",
    "Sauce Slinger": "Slingshot",
    "Lunchpad": "Launchpad",
    "Trip Shot": "Tripwire",
}

MOD_SUPPRESSED_TOOLS = {"StrabbyBall", "Slingshot", "Launchpad", "Hookshot", "Tripwire"}

# Useable Filler Items 
USE_FILLER = {
    "Ketchup!" : "Sauce_Ketchup",
    "Chocolate!" : "Sauce_Chocolate",
    "Hot Sauce!": "Sauce_HotSauce",
    "Ranch!": "Sauce_Ranch",
    "Peanut Butter!": "Sauce_PeanutButter",
    "Cheese Sauce!": "Sauce_Cheese",
}

SUPPRESSED_SAUCES = { "Sauce_Ketchup", "Sauce_Chocolate", "Sauce_HotSauce", "Sauce_Ranch", "Sauce_PeanutButter", "Sauce_Cheese" }
# (Bug Net and Snaktivator used to be here, but they've been removed from
# the item pool entirely rather than "randomised but do nothing" as it was
# confusing to players who were unaware of this.)
KNOWN_UNSUPPORTED = {}