def order_discgolfers(scores):
    players = {}
    for x in scores:
        for key,value in x.items():
            if key in players: currList = players[key]
            else: currList = ""
            players[key] = currList + str(value)
    for key in players: players[key] = players[key] [::-1] 
    players = dict(sorted(players.items(), key=lambda item: item[1]))
    return list(players.keys())


scores = [{
    'bob': 3,
    'patric': 2,
    'squidward': 4,
}, {
    'bob': 3,
    'patric': 3,
    'squidward': 3,
}, {
    'bob': 3,
    'patric': 3,
    'squidward': 2,
}, {
    'bob': 3,
    'patric': 3,
    'squidward': 3,
}]

print(order_discgolfers(scores))