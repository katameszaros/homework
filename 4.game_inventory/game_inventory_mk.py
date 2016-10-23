inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} 

def display_inventory():
    print("Inventory:")
    for key, value in inv.items():
        print(value, key)
    print("Total number of items: " + str(sum(inv.values())))


display_inventory()
