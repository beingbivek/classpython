'''
A perfect number is a positive integer that is equal to 
the sum of its proper divisors, excluding itself.
In other words, a perfect number is a number that is
the sum of all its positive divisors, 
excluding the number itself.
for eg. 6, Excluding 6 itself, the sum of the divisors is 
1 + 2 + 3 = 6.
'''
number = int(input("Enter a number: "))
perfect_num = 0

for i in range(1,number):
    if number % i == 0:
        perfect_num += i

if perfect_num == number:
    print(number," is a Perfect number.")
else:
    print(number," is not a Perfect number.")