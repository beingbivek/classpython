# a = 'softwaricacollege'
# i = 0
# while i < len(a):
#     print(a[i],'=',i)
#     i += 1

# a = 'softwaricacollege'
# i = len(a)-1
# while i >= 0:
#     print(a[i],'=',i)
#     i -= 1

# # in case of continue
# i = 0
# while i < 4:
#     if i == 2:
#         i += 1
#         continue
#     else:
#         print(i)
#     i += 1

# # Bank 

# print("Welcome to Mobile Banking")
# uname,password = 'admin','pass'
# i = 3
# while i > 0:
#     username = input("Enter your username: ")
#     passkey = input("Enter your password: ")
#     if (
#         uname != username
#         or passkey != password
#         or len(passkey) < 8
#         or username == ''
#         or passkey == ''
#     ):
#         if i == 1:
#             print(f"Wrong Username or Password, {i-1} attempts left.")
#     else:
#         print("Successful Login")
#         break
#     i -= 1
# else:
#     print("You are blocked")

# # Sum untill user input's 0
# sum = 0
# i = 1
# while i != 0:
#     usernum = int(input("Entera positive number: "))
#     sum += usernum
#     print("sum: ",sum)
#     i = usernum

# Guess the number of multiplication of two random numbers
import random
isExit = False
while (not isExit):
    a = random.randint(1,30)
    b = random.randint(1,30)
    product = a * b
    user_input = int(input("Enter your guess number: "))
    if user_input == product:
        print(f"Correct!, The product of {a} and {b} is: ",product)
    else:
        print(f"Incorrect, the answer was {product}, try again!")
    user_decision = input("Do you want to continue (y/n): ").lower()
    if user_decision == 'n':
        print("Thanks for playing")
        isExit = True