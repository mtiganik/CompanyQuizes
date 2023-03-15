def sonic_how_many_rings_did_you_get(inp):
    r = 0
    oR = ['a','q','o','p','d','b','R','Q','D','O','P','e','6','9','g','4']
    tR = ['B','8']
    for x in inp:
        if x in oR:
            r = r +1
        if x in  tR:
            r = r +2
    return r
