# # usernum = int(input('Enter a num: '))
# usernum = 5
# seq = '11'
# mid = 0
# upper = lower = 0
# # middle = '12'
# for i in range(1,usernum+1):
#     if i == 1:
#         print(i)
#     elif i == 2:
#         print(seq)
#     elif i > 2:
#         for j in range(len(seq)):
#             middle = ''
#             for k in range(2):
#                 if len(middle) <= 2:
#                     mid += int(seq[j])
#                     middle += str(mid)
#                 else:
#                     seq = '1' + str(middle) + '1'

#             # for k in range(2):
#             # mid += int(seq[j])
#         print(seq)

#     # print(seq)
#     # for j in range(i):
#     #     print(j)
        
#         # if len(seq) > 1:
#         #     mid += int(seq[j])
#         # num = int(seq[j]) * 10 + int(mid)
#         # print(num)
#         # seq = str(num)

# a = 121
# s = str(a)
# end = start = sum = 0
# lst = []
# # b = 1331
# for i in range(len(s)):
#     b = int(a % 10)
#     lst.append(b)
#     a = (a - b) / 10
# print(lst)
# while start < 3:

# for i in range(lst):
#     start += 1
#     sum += lst[i]
#     if start == 2:
#         start = i
#         break

# Get user input
num_rows = int(input("Enter the number of rows: "))

# Initialize the first row
triangle = [[1]]

# Generate Pascal's Triangle
for i in range(1, num_rows):
    row = [1]
    for j in range(1, i):
        above_left = triangle[i-1][j-1]
        above_right = triangle[i-1][j]
        row.append(above_left + above_right)
    row.append(1)
    triangle.append(row)

# Print Pascal's Triangle
for row in triangle:
    print(" ".join(map(str, row)))

