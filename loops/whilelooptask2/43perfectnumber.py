'''
perfect no are those numbers who sum of factors except themself is the number itself.
for eg. 6 => factors(1,2,3,6) => factors except themselves so, 1,2 and 3 => sum of factors is 6 hence it's a perfect number
'''
usernum = int(input('Enter a number: '))
i = 1
sum = 0
while i < usernum:
    if usernum % i == 0:
        sum += i
    i += 1
if usernum == sum:
    print('Given number is Perfect number.')
else:
    print('Given number is not Perfect number.')