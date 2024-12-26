# a = [1,2,3,4,5]
# for i in a:
#     if i == 3:
#         break
#     print(i)
# else:
#     print("Good Luck")

# a = [1,2,3,4,5]
# for i in a:
#     if i == 3:
#         continue
#     print(i)
# else:
#     print("Good Luck")

print("Welcome to Mobile Banking")
uname,password = 'admin','pass'

for i in range(3,0,-1):
    username = input("Enter your username: ")
    passkey = input("Enter your password: ")
    if (
        uname != username
        or passkey != password
        or len(passkey) < 8
        or username == ''
        or passkey == ''
    ):
        if i == 1:
            print(f"Wrong Username or Password, {i-1} attempts left.")
    else:
        print("Successful Login")
        break
else:
    print("You are blocked")

