user_input = input("Enter a long string: ")
vowel = ['a','e','i','o','u']
newstring = ''
for i in user_input:
    for v in vowel:
        if i == v:
            break
    else:
        newstring += i
print(newstring)