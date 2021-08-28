locations = {0: "You are sleeping",
             1: "You are walking on a road",
             2: "You are at the top of a hill",
             3: "You are inside a building",
             4: "You are in a valley",
             5: "You are in the forest"}
exits = [{"Q": 0},
         {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         {"N": 5, "Q": 0},
         {"W": 1, "Q": 0},
         {"N": 1, "W": 2, "Q": 0},]
dic={
    locations: exits for locations,exits in zip(locations, exits)
}
print(dic)