def order_discgolfers(scores):
    pl = {}
    for x in scores:
        for k,v in x.items():
            pl[k] = str(v) + pl.get(k, "") 
    pl = dict(sorted(pl.items()))
    pl = dict(sorted(pl.items(), key=lambda item: item[1]))
    return list(pl.keys())