mark = int(input("Enter you mark: "))
if mark > 100:
    print("Invalid Mark.")
elif mark >= 80:
    print("You got A")
elif mark >= 60:
    print("You got B")
elif mark >= 50:
    print("You got C")
elif mark >= 45:
    print("You got D")
elif mark >= 25:
    print("You got E")
elif mark >= 0:
    print("You got F")
else:
    print("Invalid Mark")
