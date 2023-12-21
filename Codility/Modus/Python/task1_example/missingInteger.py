from ast import literal_eval

f = open("test-input.txt")
vals = []
for x in f:
    val = literal_eval(x)
    vals.append(val)

#Task score of 33%
def solution(A):
    A.sort()
    lastDigit = A[len(A)-1]
    if(lastDigit <= 0): return 1
    for i in range(1,len(A)):
        if A[i] <= 0: continue
        if A[i] - A[i-1] > 1: return A[i-1] +1
    return lastDigit +1
    

for x in vals:
    print(solution(x))