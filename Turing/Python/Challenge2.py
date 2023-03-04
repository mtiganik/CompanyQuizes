
def IsValid(s):
    openStack = []  
    for i in s:
        if i == '(' or i == '[' or i == '{':
            openStack.append(i)
        else:
            lastEl = openStack[len(openStack)-1]
            if (lastEl == '(' and i == ')' ) or (lastEl == '[' and i == ']') or (lastEl == '{' and i == '}'):
                openStack.pop()
            else: return False
    return True


string = "()[]{([])(()}"
print(IsValid(string))