class1 = int(input("Enter the no. of student in Class 1: "))
class2 = int(input("Enter the no. of student in Class 2: "))
class3 = int(input("Enter the no. of student in Class 3: "))
if class1 % 2 != 0:
    class1+=1
if class2 % 2 != 0:
    class2+=1
if class3 % 2 != 0:
    class3+=1
desk1 = class1 // 2
desk2 = class2 // 2
desk3 = class3 // 2
print("Total Desk needed is: {}".format(desk1+desk2+desk3))

# Another Method
a = int(input("Enter the number of students in class 1: "))
b = int(input("Enter the number of students in class 2: "))
c = int(input("Enter the number of students in class 3: "))

if a % 2 == 0:
    desks_a = a // 2
else:
    desks_a = (a // 2) + 1

if b % 2 == 0:
    desks_b = b // 2
else:
    desks_b = (b // 2) + 1

if c % 2 == 0:
    desks_c = c // 2
else:
    desks_c = (c // 2) + 1
total_desks = desks_a + desks_b + desks_c
print(f"Total Desk needed is: {total_desks}")
