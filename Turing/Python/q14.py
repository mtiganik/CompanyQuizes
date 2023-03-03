#PseudoCode
document = (20005001, 'Brahma Gupta', (101, 132, 345), ['singing', 'quizzing'])
document[-1].append('poetry')
print(document)

#Answer: The program would run successfully since only a reference to the list is stored, 
# which is immutable, but the list pointed to by it can be safely modified