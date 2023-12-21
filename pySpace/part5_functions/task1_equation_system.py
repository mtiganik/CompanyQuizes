
def solve(*equations):
    gridDic = []
    for x in equations:
        gridDic.append(getEqData(x))
    grid = makeListFromDict(gridDic)

    for k in range(0,len(grid)-1):
        valOnTopCol = grid[k][k]
        for i in range(k+1,len(grid)):
            valToGetZero = grid[i][k]
            coefitsent = -valToGetZero/valOnTopCol
            for j in range(k,len(grid[0])):
                grid[i][j] = grid[i][j] + coefitsent*grid[k][j]

    for i in range(-1, -len(grid)-1,-1):
        sumOfOthers = 0
        for j in range(-1,i,-1):
            sumOfOthers = sumOfOthers + grid[j][-1]*grid[i][j-1]
            grid[i][j-1] = 0
        grid[i][-1] = (grid[i][-1] - sumOfOthers)/grid[i][i-1]
        grid[i][i-1] = 1

    keys = []
    for k in gridDic[0]:
        
        keys.append(list(k.keys())[0])
    keys.pop()
    resDict = {}
    for i in range(0,len(grid)):
        resDict[keys[i]] = custRound(grid[i][-1])
    return resDict
    

def custRound(num):
    val = round(num,2)
    if round(num) - val == 0: return round(num)
    return val
def makeListFromDict(dic):
    res = []
    curr = []
    for y in dic:
        for x in y:
            for value in x.values():
                curr.append(value)
        res.append(curr)
        curr = []
    return res

def getEqData(eq):
    chars = 'abcdefghijklmnopqrstuvwxyz' #all chars in list
    (eq,endVal)=(eq.split("="))
    dict = []
    for x in chars:
        if x in eq:
            (currval, eq) = eq.split(x)
            try:
                if currval in ('',"+"): currval = 1
                if currval =='-': currval = -1
                dict.append({x:float(currval)})
            except ValueError:
                raise ValueError("Non alphabetical order not implemented. Please place your variables in alphabetical order")
    dict.append({"=":float(endVal)})
    return dict
print("Hello")
solve("a+b+2c-7d=18","-5a+5b+7c-3d=-54","9a-5b-3c+9d=44","3a-3b-2c-6d=47") #want to know answer
solve("2x+3y=6","4x+9y=15") #x=1,5 y=1
solve("2e+3f=1", "0e+f=-1") # variable is 0 in one eq 
solve("0.1k-0.7m=-1.1","0.5k+0.2m=1.8") #k=-4,m=1
solve("-4x+3y-2z=-7","-8x-3y+4z=-5","16x-3y-5z=19") #x=1,y=-1,z=0
solve("2v+w+x+y+z=4","v+2w+x+y+z=5","v+w+2x+y+z=6","v+w+x+2y+z=7","v+w+x+y+2z=8")
solve("2a+2b-c+d=4","4a+3b-c+2d=6","8a+5b-3c+4d=12","3a+3b-2c+2d=6")
solve("-4a-6b+8c+7d=-21","-9a-3b-4c+d=82","-9a-b+4c-10d=111","3a-b+2c+0d=-29")
solve("7a+8b+9c+2d=-69","-5a+b+c+9d=-38","-8a+6b-4c-8d=74","9a-4b-9c+7d=-135")
 
