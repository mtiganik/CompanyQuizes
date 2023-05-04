def identify_ninja(nn, villagers):
    res = []
    for x in villagers:
        if areAnagrams(nn, x):
            res.append(x)
    return res

def areAnagrams(i1,i2):
    sl1 = list(i1)
    sl1.sort()
    sl2 = list(i2)
    sl2.sort()

    return (sl1 == sl2)