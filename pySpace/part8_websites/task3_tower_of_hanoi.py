#text starting, text middle, text ending
ts,tm,te = "starting","middle","ending"

def hanoi(N):
    s,m,e = [i for i in range(N,0,-1)],[],[]
    i = 0
    retStr = ""
    while(True):
        i += 1
        retStr = retStr + f"{i}. " + moveSmallest(s,m,e, N%2==0)
        if i == 2**N -1: 
            return retStr.strip()
        i += 1
        retStr = retStr + f"{i}. " + MoveOtherThanSmallest(s,m,e)

def switch(first, second, txtFirst, txtSecond):
    if not second: return MoveFirstToSecond(first,second,txtFirst,txtSecond)
    if not first: return MoveSecondToFirst(first,second,txtFirst,txtSecond)
    if first[-1] < second[-1]:
        return MoveFirstToSecond(first,second,txtFirst,txtSecond)
    else:
        return MoveSecondToFirst(first,second,txtFirst,txtSecond)
    
def MoveOtherThanSmallest(s,m,e):
    return switch(m,e,tm,te) if 1 in s \
else switch(s,e,ts,te) if 1 in m else switch(s,m,ts,tm)

def MoveFirstToSecond(first, second, txtFirst, txtSecond):
    second.append(first[-1])
    first.pop()
    return f"Move disk from {txtFirst} pole to {txtSecond} pole.\n"

def MoveSecondToFirst(first, second, txtFirst, txtSecond):
    first.append(second[-1])
    second.pop()
    return f"Move disk from {txtSecond} pole to {txtFirst} pole.\n"

def moveSmallest(s,m,e, isEven):
    itIsNow, whereToGo, txtNow,txtToGo =0,0,0,0
    if 1 in s:
        itIsNow, txtNow = s, ts
        (whereToGo,txtToGo)= (m,tm) if isEven==True else (e, te)
    elif 1 in m:
        itIsNow,txtNow = m, tm
        (whereToGo, txtToGo) = (e,te) if isEven == True else (s,ts)
    else:
        itIsNow,txtNow = e, te
        (whereToGo, txtToGo) = (s,ts) if isEven == True else (m,tm)
    return MoveFirstToSecond(itIsNow,whereToGo,txtNow,txtToGo)

print(hanoi(3))