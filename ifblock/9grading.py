mark = int(input("Enter your mark: "))
if mark < 70:
    print("You Failed.")
elif mark <= 79:
    print("You have scored grade C.")
elif mark <= 89:
    print("You have scored grade B.")
elif mark <= 100:
    print("You have scored grade A.")
else:
    print("Invalid Mark")