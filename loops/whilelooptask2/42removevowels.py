old = input('Enter a long string: ')
new = ''
vowels = ['a','e','i','o','u']
i = 0
while i < len(old):
    check = False
    j = 0
    while j < len(vowels):
        if old[i] == vowels[j]:
            check = True
            break
        j += 1
    if check == False:
        new += old[i]
    i += 1
print(new)