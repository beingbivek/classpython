i = 3
sum = 0
while i < 100:
    if i % 3 == 0 or i % 5 == 0:
        sum += i
    i += 1
print(sum)