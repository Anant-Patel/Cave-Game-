locations = {0: {"desc": "sitting infront of computer", #desc = description
                 "exits": {}, #exits = exits
                 "dire": {}}, #dire = directions
            1: {"desc": "standing at end of the road",
                "exits": {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
                "dire": {"2": 2, "3": 3, "5": 5, "4": 4}},
            2: {"desc": "at top of the hill",
                "exits": {"N": 5, "Q": 0},
                "dire": {"5": 5}},
            3: {"desc": "inside the building",
                "exits": {"W": 1, "Q": 0},
                "dire": {"1": 1}},
            4: {"desc": "in a valley",
                "exits": {"N": 1, "W": 2, "Q": 0},
                "dire" : {"1": 1, "2": 2}},
            5: {"desc": "in the forest",
                "exits": {"W": 2, "S":1, "Q": 0},
                "dire": {"2": 2, "1": 1}} }

# exits = { 0: {"Q": 0},
#           1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
#           2: {"N": 5, "Q": 0},
#           3: {"W": 1, "Q": 0},
#           4: {"N": 1, "W": 2, "Q": 0},
#           5: {"W": 2, "S":1, "Q": 0} }
#
# dire = {1: {"2": 2, "3": 3, "5": 5, "4": 4},
#         2: {"5": 5},
#         3: {"1": 1},
#         4: {"1": 1, "2": 2},
#         5: {"2": 2, "1": 1}}

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
    AE = ", ".join(locations[loc]["exits"].keys())

    print(locations[loc]["desc"])
    if loc == 0:
        break
    else:
        allExits = locations[loc]["exits"].copy()
        allExits.update(locations[loc]["dire"])

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
