color = input("Enter a color: ")

if color.lower() == "red":
    print("Stop")
elif color.lower() == "yellow":
    print("Slow Down")
elif color.lower() == "green":
    print("Go")
else:
    print("Invalid Signal")