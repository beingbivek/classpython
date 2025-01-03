user_num = int(input('Enter a number: '))
i = 1
fact = 1
# factorial of 5 = 1 * 2 * 3 * 4 * 5 = 120
while i <= user_num:
    fact *= i
    i += 1
print('Factorial is: ',fact)