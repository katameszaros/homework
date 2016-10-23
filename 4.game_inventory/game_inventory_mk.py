from operator import itemgetter

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


def sort(inventory, order):
    sorted_list=()
    if order=="count,asc":
        sorted_list = sorted(inv.items(), key=itemgetter(1))
    elif order=="count,desc":
        sorted_list = sorted(inv.items(), key=itemgetter(1), reverse=True)
    else:
        sorted_list = inv.items()
    return sorted_list


class TableRowPrinter:
    '''Utility that helps to print the rows of the table'''
    first_col_w = 0
    second_col_w = 0

    def __init__(self, first_col_w, second_col_w):
        self.first_col_w = first_col_w
        self.second_col_w = second_col_w

    def print(self, col1, col2):
        '''Prints one table row right justified'''
        print(col1.rjust(self.second_col_w) + col2.rjust(self.first_col_w))

    def print_separator_row(self, separator):
        '''Repeats the given separator in the whole width of the table'''
        print(separator* (self.first_col_w + self.second_col_w))


def print_table(order="empty"):
    '''Print the table ordered depending on the parameter
    count,asc - ascending by count of items
    count,desc - descending by count of items
    otherwise its unordered'''
    first_column_header = "item name"
    second_column_header = "count" 
    first_column_width = len(first_column_header)
    second_column_width = len(second_column_header)

    for key, value in inv.items():
        first_column_width = max(first_column_width, len(key))
        second_column_width = max(second_column_width, len(str(value)))

    first_column_width += 5
    print("Inventory: ")
    table_row_printer = TableRowPrinter(first_column_width, second_column_width)
    table_row_printer.print(second_column_header, first_column_header)
    table_row_printer.print_separator_row("-")
    
    sorted_list=sort(inv, order)
    
    for elem in sorted_list:
        key = elem[0]
        value = elem[1]
        table_row_printer.print(str(value), key)
    table_row_printer.print_separator_row("-")
    print("Total number of items: " + str(sum(inv.values())))


def merge_inventories(inv1, inv2):
    '''Merges the given inventories without changing them. 
    Returns the merged inventory.'''
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
    '''Imports the content of the given file as an inventory.
    Defaults to 'import_inventory.csv'.
    The file is expected to be a CSV file with the following format:

    item_name,count
    ruby,3'''
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
    '''Exports the content of the inventory to the given file.
    Defaults to 'export_inventory.csv'.'''
    with open(filename, "w") as f:
        f.write("{0},{1}\n".format("item_name", "count"))
        for key, value in inv.items():
            f.write("{0},{1}\n".format(key, value))
        
        
    
inv = add_to_inventory(inv, dragon_loot)
#import_inventory()
print_table("count,desc")
export_inventory()



