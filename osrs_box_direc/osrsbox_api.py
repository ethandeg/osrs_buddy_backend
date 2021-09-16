from osrsbox import items_api
print('__file__={0:<35} | __name__={1:<25} | __package__={2:<25}'.format(__file__,__name__,str(__package__)))
items = items_api.load()


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

# def filter_items(filters):
#     valid = validate_item_filter(filters)
#     items_to_filter = items.copy()
#     if valid:
#         for filter in filters:
#             items_to_filter = [i for i in items_to_filter if i[filter].lower() == ]