from collections import OrderedDict
from operator import getitem




def sort_footy(teams):
    # res = sorted(teams, key=lambda 
    #              x:((1000-teams[x]['wins']),teams[x]['games_played'],teams[x]['name'] ))
    
    #res = sorted(teams.items(), key=lambda x:
    # ( (1000-x[1]['wins']),x[1]['games_played'], x[1]['name']) )
    # x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
    res= {k: v for k, v in sorted(teams.items(), key=lambda x: 
                                  ( (1000-x[1]['wins']),x[1]['games_played'], x[1]['name']))}
     
    #print(type(res[1]))
    return res

def sortFn(x):
    print(x)
    return 0
teams1 ={
    "1ccc" : {
        "name":"ccc",
        "wins": 15,
        "games_played":20
    },
    "2aaa" : {
        "name":"aaa",
        "wins": 15,
        "games_played":30

    },
    "3bbb": {
        "name":"bbb",
        "wins": 2,
        "games_played":6

    }
}
teams = {
    'Arsenal FC': {
        'name': 'Arsenal FC',
        'wins': 4,
        'games_played': 62,
    },
    'Chelsea FC': {
        'name': 'Chelsea FC',
        'wins': 6,
        'games_played': 16,
    },
    'Madrid Real': {
        'name': 'Madrid Real',
        'wins': 3,
        'games_played': 118,
    },
    'Barcelona FC': {
        'name': 'Barcelona FC',
        'wins': 4,
        'games_played': 81,
    }
}
sort_footy(teams1)



# test_dict = {'Nikhil' : { 'roll' : 24, 'marks' : 17},
#              'Akshat' : {'roll' : 54, 'marks' : 12},
#              'Akash' : { 'roll' : 12, 'marks' : 15}}
 
# # printing original dict
# print("The original dictionary : " + str(test_dict))
 
# # using OrderedDict() + sorted()
# # Sort nested dictionary by key
# res = OrderedDict(sorted(test_dict.items(),
#        key = lambda x: getitem(x[1], 'marks')))
 
# # print result
# print("The sorted dictionary by marks is : " + str(res))