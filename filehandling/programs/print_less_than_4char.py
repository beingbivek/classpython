def display():
    with open(r'D:\Bivek Study Files\Python Coding\filehandling\programs\softwarica.txt') as f:
        lines = f.readlines()
        for line in lines:
            words = line.split()
            for word in words:
                if len(word) < 5:
                    print(word)
display()