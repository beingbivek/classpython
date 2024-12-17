color = input("Enter a Traffic Light Color: ").lower()
color = color.lower()
if color == "red":
    print("Stop")
elif color == "yellow":
    print("Get Ready")
elif color == "green":
    print("GO!")
else:
    print("Invalid Input")
