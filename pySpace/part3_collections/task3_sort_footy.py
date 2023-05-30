from collections import OrderedDict
from operator import getitem




def sort_footy(teams):
    # res = sorted(teams, key=lambda 
    #              x:((1000-teams[x]['wins']),teams[x]['games_played'],teams[x]['name'] ))
    
    #res = sorted(teams.items(), key=lambda x:
    # ( (1000-x[1]['wins']),x[1]['games_played'], x[1]['name']) )

    # res= {k: v for k, v in sorted(teams.items(), key=lambda x: 
    #                               ( (1000-x[1]['wins']),x[1]['games_played'], x[1]['name']))}
    
    res= dict(sorted(teams.items(), key=lambda x:
                 ( (1000-x[1]['wins']),x[1]['games_played'], x[1]['name'])))
    list = []
    for k in res.items(): list.append(k[1])
    # res = list(res.items())
    return list

teams = {
    'Arsenal FC': {
        'name': 'Arsenal FC',
        'wins': 4,
        'games_played': 62,
        'wins_against_teams': {
            'Chelsea FC': 1,
            'Madrid Real': 2,
            'Barcelona FC': 1
        }
    },
    'Chelsea FC': {
        'name': 'Chelsea FC',
        'wins': 6,
        'games_played': 16,
        'wins_against_teams': {
            'Arsenal FC': 4,
            'Madrid Real': 0,
            'Barcelona FC': 2
        }
    },
    'Madrid Real': {
        'name': 'Madrid Real',
        'wins': 3,
        'games_played': 118,
        'wins_against_teams': {
            'Arsenal FC': 0,
            'Chelsea FC': 3,
            'Barcelona FC': 0
        }
    },
    'Barcelona FC': {
        'name': 'Barcelona FC',
        'wins': 4,
        'games_played': 81,
        'wins_against_teams': {
            'Arsenal FC': 0,
            'Madrid Real': 0,
            'Chelsea FC': 4
        }
    }
}


sort_footy(teams)


