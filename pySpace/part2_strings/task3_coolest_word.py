def coolest_word(inp):
    data = []
    for x in inp:
        data.append([x,len(set(x))])
    max = 0
    for x in data:
        if x[1] > max:
            max = x[0]
    return max




print(coolest_word(['expectation', 'discomfort', 'half', 'decomposition']))