count_of_doors = 101
doors = [False] * count_of_doors

def change_door_status():
    for i in range(count_of_doors):
        for j in range(0, count_of_doors, i+1):
            doors[j] = not doors[j]

def collect_open_doors():
    open_doors = ""
    for i in range(1, count_of_doors):
        if doors[i] == True:
            open_doors += str(i) + ", "
    return open_doors

change_door_status()
open_doors = collect_open_doors()
print("The following doors remained open: " + open_doors)
    
