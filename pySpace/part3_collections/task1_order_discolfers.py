# import numpy as np

def order_discgolfers(scores):
    players = {}
    for x in scores:
        for key,value in x.items():
            players[key] = str(value) + players.get(key, "") 
    players = dict(sorted(players.items()))
    players = dict(sorted(players.items(), key=sortOrder))
    return list(players.keys())

def sortOrder(item):
    return item[1]

# scores = [{
#     'AA': 4,
#     'CC': 1,
#     'DD': 3,
#     'BB': 3,
# }, {
#     'AA': 3,
#     'CC': 3,
#     'DD': 3,
#     'BB': 3,
    
# }, {
#     'AA': 3,
#     'CC': 3,
#     'DD': 3,
#     'BB': 3,
# }, {
#     'AA': 2,
#     'CC': 2,
#     'DD': 2,
#     'BB': 2,
# }]

# print(order_discgolfers(scores))