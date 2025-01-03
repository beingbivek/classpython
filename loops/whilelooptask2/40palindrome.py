usernum = input('Enter a long number: ')
reversenum = ''
i = len(usernum) - 1
while i >= 0:
    reversenum += usernum[i]
    i -= 1
if reversenum == usernum:
    print('Given number is a pallindrome.')
else:
    print('Given number is not a pallindrome.')