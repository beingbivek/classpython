# Accept five names from the user and write in a file 'softwarica.txt' (each name should write in separate line)?

with open(r'D:\Bivek Study Files\Python Coding\filehandling\programs\softwarica.txt', 'w') as file:
    for i in range(5):
        name = input(f"Enter {i} name: ")
        file.write(name + '\n')
