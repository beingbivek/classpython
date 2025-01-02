print("Welcome to Mobile Banking")
uname,password = 'admin','pass'
i = 3
while i > 0:
    username = input("Enter your username: ")
    passkey = input("Enter your password: ")
    if (
        uname != username
        or passkey != password
        or username == ''
        or passkey == ''
    ):
        if i != 1:
            print(f"Wrong Username or Password, {i-1} attempts left.")
    else:
        print("Successful Login")
        break
    i -= 1
else:
    print("You are blocked")