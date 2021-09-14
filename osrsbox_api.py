from osrsbox import items_api

items = items_api.load()

item = [i for i in items if i.name.lower() == 'bandos godsword'.lower()]

def get_item_by_name(name):
    return [i for i in items if i.name.lower() == name.lower()]