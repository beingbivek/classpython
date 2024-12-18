mark = int(input("Enter your Mark(0-100): "))
if mark < 25 and mark >= 0:
    grade = 'D'
elif mark < 45:
    grade = 'C'
elif mark < 50:
    grade = 'B'
elif mark < 60:
    grade = 'B+'
elif mark < 80:
    grade = 'A'
elif mark <= 100:
    grade = 'A+'
else:
    grade = 'wrong'

if grade == 'wrong':
    print('Incorrect Mark!')
else:
    print(f"Your grade is: {grade}")