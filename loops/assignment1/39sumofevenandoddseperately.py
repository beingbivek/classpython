sum_of_odd = 0
sum_of_even = 0
for i in range(1,101):
    if i % 2 != 0:
        sum_of_odd += i
    else:
        sum_of_even += i
print("The sum of odd numbers is: ",sum_of_odd)
print("The sum of even numbers is: ",sum_of_even)