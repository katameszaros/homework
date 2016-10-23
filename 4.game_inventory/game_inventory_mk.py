
inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} 
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def display_inventory():
    print("Inventory:")
    for key, value in inv.items():
        print(value, key)
    print("Total number of items: " + str(sum(inv.values())))

def add_to_inventory(inventory, added_items):
    for i in added_items:
        if i in inventory.keys():
            count = inventory.get(i)
            count += 1
            inventory[i] = count
        else:
            inventory[i]=1
    return inventory

inv = add_to_inventory(inv, dragon_loot)

display_inventory()

