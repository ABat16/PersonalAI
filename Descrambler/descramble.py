file = open('words.txt', 'r', encoding='utf-8')
words = []

for line in file:
    if line != '\n':
        word = line.split(' ')[0].strip('\n').strip('')
        words.append(str(word.lower()))

scrambled = input("Enter Letters: ")
for word in words:
    if len(word) == len(scrambled):
        Equal = True
        for letter in scrambled:
            if word.count(letter) != scrambled.count(letter):
                Equal = False
        if Equal:
            print(word)

   


