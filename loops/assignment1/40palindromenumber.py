number = input("Enter a large number: ")
reversenumber = ''
for i in range(len(number)-1,-1,-1):
    reversenumber += number[i]
# print(reversenumber)
if number == reversenumber:
    print(number," is Palindrome.")
else:
    print(number,"is not a Palindrome number.")