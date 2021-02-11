locations = {0: "will study",
                1: "at 322",
                2: "at 325",
                3: "at 396",
                4: "at 333",
                5: "at 496"}

exits = [{"Q": 0},
            {"W": 3, "E": 4, "S": 5, "N": 2, "Q": 0},
            {"S": 1, "Q": 0},
            {"N": 2, "E": 1, "Q": 0},
            {"S": 5, "Q": 0},
            {"E": 4, "Q": 0}]

loc = 1
while True:
    avaExi = ""
    for i in exits[loc].keys():
        avaExi += ", " + i

    print(locations[loc])

    if loc == 0:
        break

    directions = input("available areas are" + avaExi + "").upper()
    print()

    if directions in exits[loc]:
        loc = exits[loc][directions]
    else:
        print("Please enter valid direction ")
