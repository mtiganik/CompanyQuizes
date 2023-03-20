def make_list(number):
    names = []
    for item in range(0,number):
        names.append(input("Enter your name with capital letter"))
    return names

number = int(input("how many names need to be enter?"))
names = make_list(number)
for name in names:
    if name [1] == "A":
        print("Name ", name, " starts with A")