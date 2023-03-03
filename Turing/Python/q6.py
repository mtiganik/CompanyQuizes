pararaph = ["My first sentence", "second sentence", "My thrid nice sentence"]
singleWordList =[]
for sentence in pararaph:
    for word in sentence.split():
        singleWordList.append(word)

print(singleWordList)
singleWordList = []
singleWordList = [word for sentence in pararaph for word in sentence]
print(singleWordList)

singleWordList = []
singleWordList = [word for word in sentence for sentence in pararaph]
print(singleWordList)

singleWordList = []
singleWordList = [word for word in sentence.split() for sentence in pararaph]
print(singleWordList)

singleWordList = []
singleWordList = [word for sentence in pararaph for word in sentence.split()]
print(singleWordList)