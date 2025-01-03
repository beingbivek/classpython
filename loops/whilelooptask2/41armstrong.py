'''
Armstring number is that number:
153 => 3 digits 1,5,3 => 1**3 + 5**3 + 3**3 = 153
sum of no. of digits powered to each digits == the original no then it is armstrong.
'''
usernum = input('Enter a number: ')
i = armnum = 0
power = len(usernum)
while i < len(usernum):
    armnum += int(usernum[i])**power
    print(armnum)
    i += 1
if int(usernum) == armnum:
    print('The number is armstring')
else:
    print('The number is not armstring')
    