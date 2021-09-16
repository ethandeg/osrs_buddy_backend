from osrsbox import items_api
print('__file__={0:<35} | __name__={1:<25} | __package__={2:<25}'.format(__file__,__name__,str(__package__)))
items = items_api.load()

item = [i for i in items if i.name.lower() == 'bandos godsword'.lower()]

def get_item_by_name(name):
    return [i for i in items if i.name.lower() == name.lower()]

def validate_item_filter(filters):
    valid_filters = ['id', 'name', 'members', 'tradeable', 'stackable', 'noted', 'noteable', 'equipable', 'cost'
                    'cost', 'lowalch','highalch', 'weight', 'buy_limit', 'quest_item', 'release_date', 'examine','url'
    ]
    for filter in filters:
        if filter not in valid_filters:
            return False
    return True
#     print(item.id)           # Item ID number
# print(item.name)         # In-game name
# print(item.members)      # Boolean if members item
# print(item.tradeable)    # Boolean if the item tradeable
# print(item.stackable)    # Boolean if the item stackable
# print(item.noted)        # Boolean if the item noted
# print(item.noteable)     # Boolean if the item noteable
# print(item.equipable)    # Boolean if the item equipable
# print(item.cost)         # Store cost price
# print(item.lowalch)      # Low alchemy value
# print(item.highalch)     # High alchemy value
# print(item.weight)       # Weight of the item (in kgs)
# print(item.buy_limit)    # Item buy limit at GE
# print(item.quest_item)   # List of quests an item is associated with
# print(item.release_date) # Release date of the item
# print(item.examine)      # Examine text of item
# print(item.url)          # OSRS Wiki URL (uses new wiki, not Wikia)