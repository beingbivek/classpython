# Write a program to read first 5 characters from a file name 'softwarica.txt'?
with open(r'D:\Bivek Study Files\Python Coding\filehandling\programs\softwarica.txt', 'r') as file:
    content = file.read(5)
    print(content)
