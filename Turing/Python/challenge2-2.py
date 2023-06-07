def solution(k):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    ans = []
    xdem = [0]
    for x in xdem:
        isHere = True
        for j in range(1,len(k)):
            if x not in k[j]:
                isHere = False
                break
        if isHere == True:
            ans.append[x]
            for y in range(1,len(k)):



solution(["elli","nelli","collie"])