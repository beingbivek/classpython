radius = float(input("Enter the radius of the circle: "))
pi = 3.14
if radius >= 0:
    area = pi * radius ** 2
    print(f"The area of the circle is {area}")
else:
    print("Invalid radius!")
