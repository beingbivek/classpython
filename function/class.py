# Args
# def add(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum
# print(add(10,20,30,40,50))

# Kwargs
# def add(**k):
#     sum = 0
#     for i in k:
#         sum += i
#     return sum
# print(add(a=10,20,30,40,50))


# Nested Functions
# Helper Functions
# def outer():
#     pocket_money = 10
#     print(pocket_money)
#     def inner():
#         c = pocket_money + 30
#         print(c)
#     inner()

# outer()

# Helper Function but the inner function is accessible on the main program

# def outer():
#     pocket_money = 10
#     print(pocket_money)
#     def inner():
#         c = pocket_money + 30
#         print(c)
#     return inner

# # print(outer()())
# c = outer()
# c()


# # LEGB rule example
# from math import * # Builtin Var for pi
# pi = 10 # Global Var
# def outer():
#     pi = 20 # Enclosed/non-Local Var
#     def inner():
#         pi = 30 # Local Var
#         print(pi)
#     inner()
# print('good luck')
# outer()
# print('good morning')

# Lambda
from functools import reduce
li = [1,2,3,4,5]
sum = reduce((lambda x,y:x+y),li)
print(sum)