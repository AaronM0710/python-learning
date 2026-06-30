stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'emerald']

def add_to_inventory(inventory, added_items):


    #check if item is already in our inventory
    for item in added_items:
      
        #if its in our inventory just increase the count
        #if not in our inventory, create a new key for it with the count set to 1
        inventory.setdefault(item,0)
        inventory[item] += 1
    return inventory


add_to_inventory(stuff, dragon_loot)