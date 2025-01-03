user_list = []
howmany = int(input('How many numbers are you going to enter: '))
i = 0
while i < howmany:
    num = int(input(f'Enter number {i + 1}: '))
    user_list.append(num)
    i += 1

even_sum = 0
i = 0
while i < len(user_list):
    if user_list[i] % 2 == 0:
        even_sum += user_list[i]
    i += 1
print('sum of even numbers in list is: ',even_sum)