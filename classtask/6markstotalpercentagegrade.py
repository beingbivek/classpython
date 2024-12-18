name = input("Enter your name: ")
science = int(input("Enter your marks in science: "))
math = int(input("Enter your marks in math: "))
social = int(input("Enter your marks in social: "))
computer = int(input("Enter your marks in computer: "))
total = science + math + social + computer
percent = (total / 400) * 100

if percent < 40:
    grade = 'fail'
elif percent < 60:
    grade = 'pass'
elif percent < 70:
    grade = 'first division'
else:
    grade = 'distinction'

print(f"Report Card of {name.title()}")
print(f"Subjects\tMarks\nScience\t{science}\nMath\t{math}\nSocial\t{social}\nComputer\t{computer}\nTotal\t{total}\nPercentage\t{percent}\nGrade\t{grade.title()}".expandtabs(tabsize=15))