# # Print A
# for row in range(6):
#     for col in range(5):
#         if row != 0 and (col == 0 or col == 4):
#             print("*",end=" ")
#         elif (col == 1 or col == 2 or col == 3) and (row == 0 or row == 3):
#             print("*",end=" ")
#         else:
#             print(end="  ")
#     print()

# # print G
# for row in range(7):
#     for col in range(4):
#         if (col == 0) and (row != 0 and row != 6):
#             print("*",end=" ")
#         elif (col == 1) and (row == 0 or row == 6):
#             print("*",end=" ")
#         elif col == 2 and (row == 0 or row == 4 or row == 6):
#             print("*",end=" ")
#         elif col == 3 and (row == 0 or row == 4 or row == 5 or row == 6):
#             print("*",end=" ")
#         else:
#             print(end="  ")
#     print()

# Print BIVEK
for row in range(7):
    for col in range(29):
        if col == 0 or col == 7 or col == 19 or col == 24:
            print("*",end=" ")
        elif (col == 1 or col == 2 or col == 20 or col == 21 or col == 22 )and (row == 0 or row == 3 or row == 6):
            print("*",end=" ")
        elif (col == 3) and (row != 0 and row != 6):
            print("*",end=" ")
        elif (col == 5 or col == 6 or col == 8 or col == 9) and (row == 0 or row == 6):
            print("*",end=" ")
        elif (col == 11 or col == 17) and (row == 0):
            print("*",end=" ")
        elif (col == 12 or col == 16) and (row == 2):
            print("*",end=" ")
        elif (col == 13 or col == 15) and (row == 4):
            print("*",end=" ")
        elif (col == 14) and row == 6:
            print("*",end=" ")
        elif (col == 25) and (row == 2 or row == 4):
            print("*",end=" ")
        elif (col == 26) and (row == 1 or row == 5):
            print("*",end=" ")
        elif (col == 27) and (row == 0 or row == 6):
            print("*",end=" ")            
        else:
            print(end= "  ")
    print()

