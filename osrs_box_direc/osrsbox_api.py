from osrsbox import items_api
print('__file__={0:<35} | __name__={1:<25} | __package__={2:<25}'.format(__file__,__name__,str(__package__)))
items = items_api.load()

item = [i for i in items if i.name.lower() == 'bandos godsword'.lower()]

def get_item_by_name(name):
    return [i for i in items if i.name.lower() == name.lower()]