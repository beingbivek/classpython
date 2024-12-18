total_days = int(input("Enter the total number of days: "))
absent_days = int(input("Enter the total number of days absent: "))
attended_days = total_days - absent_days
attendance_percentage = (attended_days / total_days) * 100
print(f"Attendance Percentage: {attendance_percentage}%")

if attendance_percentage >= 75:
    print("The student can sit for the exam.")
else:
    print("The student cannot sit for the exam.")