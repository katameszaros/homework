
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

def print_header(first_column_width, second_column_width,first_column_header, second_column_header):
    print(second_column_header.rjust(second_column_width) + first_column_header.rjust(first_column_width))

def print_table():
    copy_inv = dict(inv)
    first_column_header = "item name"
    second_column_header = "count" 
    copy_inv[second_column_header] = first_column_header
    first_column_width = 0
    second_column_width = 0

    for key, value in copy_inv.items():
        first_column_width = max(first_column_width, len(key))
        second_column_width = max(second_column_width, len(str(value)))

    first_column_width += 5
    print("Inventory: ")
    print_header(first_column_width, second_column_width, first_column_header, second_column_header)

    print('-'* (first_column_width + second_column_width))

    for key, value in inv.items():
        print(str(value).rjust(second_column_width) + key.rjust(first_column_width))
    print('-'* (first_column_width + second_column_width))
    print("Total number of items: " + str(sum(inv.values())))


def merge_inventories(inv1, inv2):
    merged = dict(inv1)
    print(inv2)
    for key, value in inv2.items():
        if key in merged.keys():
            count = merged.get(key)
            count += value
            merged[key] = count
        else:
            merged[key]= value
    return merged

def import_inventory(filename="import_inventory.csv"):
    d = {}
    with open(filename) as f:
        lines = f.readlines()
        for i in range(1, len(lines)):
            line=lines[i]
            (key, value) = line.split(",")
            d[key] = int(value)
    global inv
    inv = merge_inventories(inv, d)

def export_inventory(filename="export_inventory.csv"):
    with open(filename, "w") as f:
        f.write("{0},{1}\n".format("item_name", "count"))
        for key, value in inv.items():
            f.write("{0},{1}\n".format(key, value))
        


    
import_inventory()
print_table()
export_inventory()



