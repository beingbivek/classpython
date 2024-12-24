word = input("Enter a word: ")
for i in range(len(word)):
    if i % 2 == 0:
        print(f'{i} = {word[i]}')
