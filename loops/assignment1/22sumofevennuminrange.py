number = int(input("Enter a number: "))
sum_of_even = 0
for i in range(number+1):
    if i % 2 == 0:
        sum_of_even += i
print("The sum of even numbers is: ",sum_of_even)