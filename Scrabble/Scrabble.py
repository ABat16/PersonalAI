words = open('words.txt', 'r')
key = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', '&', "'",'/']
letters = ['t','a','b','l','e','t']
scrabble = []
raw = input("Enter Letters: ")
letters = list(raw)
for letter in letters:
    try:
        key.remove(letter)
    except:
        continue
for word in words:
    word = word.split()
    word = word[0]
    word = word.strip('\n')
    coin = True
    coin2 = True
    broken = list(word)
    for val in key:
        if val in broken:
            coin = False
    if coin:
        temp = letters.copy()
        for char in broken:
            try:
                temp.remove(char)
            except:
                coin2 = False
    if coin and coin2:
        scrabble.append(word)
        
        
for val in scrabble:
    print(val)
    
    
