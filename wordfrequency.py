infile = ('sometext.txt', 'r')
print(infile)

character = [',','.']

with open('sometext.txt') as text:
    for line in text:
        for i in character:
            line = line.replace(i,'')
        words = line.split()
        chosenword = dict((word, words.count(word))for word in set(words))

print(chosenword)
