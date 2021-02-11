locations = {0: "sitting infront of computer",
             1: "standing at end of the road",
             2: "at top of the hill",
             3: "inside the building",
             4: "in a valley",
             5: "in the forest"}

exits = { 0: {"Q": 0},
          1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q":0},
          2: {"N": 5, "Q": 0},
          3: {"w": 1, "Q": 0},
          4: {"N": 1, "W": 2, "Q": 0},
          5: {"W": 2, "S":1, "Q": 0} }

vocab = { "QUIT": "Q",
          "NORTH": "N",
          "EAST": "E",
          "WEST": "W",
          "SOUTH": "S" }

loc = 1
while True:
    availableexits = ", ".join(exits[loc].keys())
    # for directions in exits[loc].keys():
    #     availableexits += directions + ", "

    print(locations[loc])

    if loc == 0:
        break

    directions = input("available exits are " + availableexits).upper()
    print()

    # (1) if len(directions) > 1:
    #     for word in vocab:
    #         if word in directions:
    #             directions = vocab[word]

# (2)
    words = directions.split()
    for word in words:
        if word in vocab:
            directions = vocab[word]

    if directions in exits[loc]:
        loc = exits[loc][directions]
    else:
        print("you cannot go this direction")
