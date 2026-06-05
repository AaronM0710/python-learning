test_dict = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def display_inventory(inventory_dictionary):
    print('Inventory:')
    counter = 0
    for key, value in inventory_dictionary.items():
        print(str(value) + ' ' + key)
        counter += value
    print('total number of items: ' +  str(counter))





display_inventory(test_dict)