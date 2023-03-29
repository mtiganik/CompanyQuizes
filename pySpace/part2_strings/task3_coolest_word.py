def coolest_word(inp):
    data = []
    for x in inp:
        data.append([x,len(set(x))])
    max = 0
    res = None
    for x in data:
        if x[1] > max:
            max = x[1]
            res = x[0]
    return res


print(coolest_word(['expectation', 'discomfort', 'half', 'decomposition']))