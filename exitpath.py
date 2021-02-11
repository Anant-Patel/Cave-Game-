locations = {0: "sitting infront of computer",
            1: "standing at end of the road",
            2: "at top of the hill",
            3: "inside the building",
            4: "in a valley",
            5: "in the forest"}

exits = [{"Q": 0},
        {"W": 2, "E": 3, "N": 5, "S": 4, "Q":0},
        {"N": 5, "Q": 0},
        {"w": 1, "Q": 0},
        {"N": 1, "w": 2, "Q": 0},
        {"W": 2, "S":1, "Q": 0}]

loc = 1
while True:
    availableexits = ""
    for directions in exits[loc].keys():
        availableexits += directions + ", "

    print(locations[loc])

    if loc == 0:
        break

    directions = input("available exits are " + availableexits).upper()
    print()
    
    if directions in exits[loc]:
        loc = exits[loc][directions]
    else:
        print("you cannot go this direction")
