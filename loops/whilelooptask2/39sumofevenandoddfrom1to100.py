i = 1
sumofeven = sumofodd = 0
while i <= 100:
    if i % 2 == 0:
        sumofeven += i
    else:
        sumofodd += i
    i += 1
print('The sum of even no is',sumofeven,'and odd no is',sumofodd)