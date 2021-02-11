locations = {0: "sitting infront of computer",
            1: "standing at end of the road",
            2: "at top of the hill",
            3: "inside the building",
            4: "in a valley",
            5: "in the forest"}

exits = { 0: {"Q": 0},
          1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
          2: {"N": 5, "Q": 0},
          3: {"W": 1, "Q": 0},
          4: {"N": 1, "W": 2, "Q": 0},
          5: {"W": 2, "S":1, "Q": 0} }

dire = {1: {"2": 2, "3": 3, "5": 5, "4": 4},
        2: {"5": 5},
        3: {"1": 1},
        4: {"1": 1, "2": 2},
        5: {"2": 2, "1": 1}}

vocab = { "QUIT": "Q",
          "NORTH": "N",
          "EAST": "E",
          "WEST": "W",
          "SOUTH": "S",
          "ROAD": "1",
          "HILL": "2",
          "BUILDING": "3",
          "VALLEY": "4",
          "FOREST": "5" }

loc = 1
while True:
    AE = ", ".join(exits[loc].keys())

    print(locations[loc])

    if loc == 0:
        break
    else:
        allExits = exits[loc].copy()
        allExits.update(dire[loc])

    d = input("Available Exits are " + AE + " ").upper()
    # print(allExits)

    if len(d) > 1:
        for word in vocab:
            if word in d:
                d = vocab[word]

    # if len(d) > 1:
    #     words = d.split()
    #     for word in words:
    #         if word in vocab:
    #             d = vocab[word]
    #             break

    if d in allExits:
        loc = allExits[d]
    else:
        print("Please enter valid direction")
