sum = 0
for i in range(3,100):
    if i % 3 == 0 or i % 5 == 0:
        sum += i
print('Sum is: ',sum)