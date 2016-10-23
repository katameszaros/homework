'''table_data = [['a', 'b', 'c'], ['aaaaaaaaaa', 'b', 'c'], ['a', 'bbbbbbbbbb', 'c']]
for row in table_data:
    print("{: >20} {: >20} {: >20}".format(*row))'''

'''def get_pair(line):
  key, sep, value = line.strip().partition(",")
  return int(key), value

with open("import_inventory.csv") as fd:    
    d = dict(get_pair(line) for line in fd)
    print(dict)'''

d = {}
with open("import_inventory.csv") as f:
    for line in f:
       (key, val) = line.split()
       d[int(key)] = val
