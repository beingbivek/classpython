numbers=[0,1,2,3,4,5,6]
i = 0
while i < len(numbers):
    if numbers[i] == 3 or numbers[i] == 6:
        i += 1
        continue
    print(numbers[i])
    i += 1