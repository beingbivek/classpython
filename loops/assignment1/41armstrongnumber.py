number = input("Enter a number: ")
armnum = 0
for i in range(len(number)):
    # print(i)
    armnum += int(number[i])**len(number)
# print(armnum)
if int(number) == armnum:
    print(number," is Armstrong Number.")
else:
    print(number,"is not a Armstrong number.")