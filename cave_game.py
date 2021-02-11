import shelve

locations = shelve.open("location")
vocabularies = shelve.open("vocabulary")

loc = "1"
while True:
    AE = ", ".join(locations[loc]["exits"].keys())

    print(locations[loc]["desc"])
    if loc == "0":
        break
    else:
        allExits = locations[loc]["exits"].copy()
        allExits.update(locations[loc]["dire"])

    d = input("Available Exits are " + AE + " ").upper()
    # print(allExits)

    if len(d) > 1:
        for word in vocabularies:
            if word in d:
                d = vocabularies[word]

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


locations.close()
vocabularies.close()
