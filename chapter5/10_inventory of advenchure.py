stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 
             'dagger': 1, 'arrow': 12}

dragon_loot = ['gold coin', 'dagger', 'gold coin', 
               'gold coin', 'ruby', 'gold coin', 'gold coin',
               'dead rat']

new_stuff = {}

def display_inventory():
    print('Inventory')
    item_total = 0
    for k, v in stuff.items():
        print(str(v) + ' ' + k)
        item_total += v
    print('Total number of items ' + str(item_total))

for i in dragon_loot:
    new_stuff = stuff
    if i not in stuff.keys():
        new_stuff[i] = 1
    elif i in stuff.keys():
        new_stuff[i] = stuff[i] + 1

display_inventory()
