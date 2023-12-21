from ast import literal_eval

f = open("task2.txt")
vals = []
for x in f:
    x = x.split(";")
    A = literal_eval(x[0])
    B = literal_eval(x[1])
    vals.append([A,B])

def currentArraysAreSuitable(A,B):
    for i in range(0,len(A)):
        if A[i] == B[i]: return False
    return True

def rotateB(input):
    return input[-1:] + input[:-1]

def solution(A, B):
    if len(A) != len(B): raise Exception("These arrays need to have same length") 
    for i in range(0,len(A)):
        #Check if current suitable:
        if(currentArraysAreSuitable(A,B)):
            return i
        B = rotateB(B)
    return -1

for x in vals:
    print(solution(x[0], x[1]))