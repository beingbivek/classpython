number = int(input("Enter a number: "))
sum_of_odd = 0
for i in range(number+1):
    if i % 2 != 0:
        sum_of_odd += i
print("The sum of odd numbers is: ",sum_of_odd)