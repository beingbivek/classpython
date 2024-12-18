first_number = int(input("Enter your 1st number: "))
second_number = int(input("Enter your 2nd number: "))

# 1st method
print(first_number,second_number)
first_number,second_number = second_number,first_number
print(first_number,second_number)

#2nd method
print(first_number,second_number)
first_number = first_number ^ second_number
second_number = first_number ^ second_number
first_number = first_number ^ second_number
print(first_number,second_number)

#3rd method
print(first_number,second_number)
tempnumber = first_number
first_number = second_number
second_number = tempnumber
print(first_number,second_number)
