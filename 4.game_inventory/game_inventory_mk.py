
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

def print_header(first_column_width, second_column_width):
    print("count".rjust(second_column_width) + "item name".rjust(first_column_width))

def print_table():
    copy_inv = dict(inv)
    copy_inv["count"] = "item name"
    first_column_width = 0
    second_column_width = 0

    for key, value in copy_inv.items():
        first_column_width = max(first_column_width, len(key))
        second_column_width = max(second_column_width, len(str(value)))

    first_column_width += 5
    print("Inventory: ")
    print_header(first_column_width, second_column_width)

    print('-'* (first_column_width + second_column_width))

    for key, value in inv.items():
        print(str(value).rjust(second_column_width) + key.rjust(first_column_width))
    print('-'* (first_column_width + second_column_width))
    print("Total number of items: " + str(sum(inv.values())))
#display_inventory()
print_table()

