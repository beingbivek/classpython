score = int(input("Enter the subject score: "))

if score > 90:
    print("Congratulations on your score!!")
elif score >= 50 and score <= 90:
    print("Good effort! There's room for improvement.")
else:
    print("Consider retaking the course for better understanding.")
