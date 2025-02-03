def count_lines_not_starting_with_T(filename):
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            if not line.startswith('T'):
                count += 1
    return count

filename = r'D:\Bivek Study Files\Python Coding\filehandling\programs\story.txt'
result = count_lines_not_starting_with_T(filename)
print(f"Number of lines not starting with 'T': {result}")
