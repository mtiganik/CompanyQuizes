def sort_footy(teams):    
    res= dict(sorted(teams.items(), key=lambda x:
                 ((-x[1]['wins']),x[1]['games_played'], x[1]['name'])))
    list = []
    for k in res.items():list.append(k[1])
    return list