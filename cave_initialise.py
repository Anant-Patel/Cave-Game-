import shelve

locations = shelve.open("location")

locations["0"] = {"desc": "sitting infront of computer", #desc = description
                  "exits": {}, #exits = exits
                  "dire": {}} #dire = directions
locations["1"] = {"desc": "standing at end of the road",
                  "exits": {"W": '2', "E": '3', "N": '5', 'S': '4', "Q": '0'},
                  "dire": {"2": '2', "3": '3', "5": '5', "4": '4'}}
locations["2"] = {"desc": "at top of the hill",
                  "exits": {"N": '5', "Q": '0'},
                  "dire": {"5": '5'}}
locations["3"] = {"desc": "inside the building",
                  "exits": {"W": '1', "Q": '0'},
                  "dire": {"1": '1'}}
locations["4"] = {"desc": "in a valley",
                  "exits": {"N": '1', "W": '2', "Q": '0'},
                  "dire" : {"1": '1', "2": '2'}}
locations["5"] = {"desc": "in the forest",
                  "exits": {"W": '2', "S":'1', "Q": '0'},
                  "dire": {"2": '2', "1": '1'}}

locations.close()

vocabularies = shelve.open("vocabulary")

vocabularies["QUIT"] = "Q"
vocabularies["NORTH"] = "N"
vocabularies["EAST"] = "E"
vocabularies["WEST"] = "W"
vocabularies["SOUTH"] = "S"
vocabularies["ROAD"] = "1"
vocabularies["HILL"] = "2"
vocabularies["BUILDING"] = "3"
vocabularies["VALLEY"] = "4"
vocabularies["FOREST"] = "5"

vocabularies.close()
