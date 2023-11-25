file = open("boards.txt", 'a')
for i in range(5):
    for j in range(5):
        val = input("space: ")
        file.write(val)
        if j != 4:
            file.write(',')
    file.write('\n')
file.write('\n')
file.close()
