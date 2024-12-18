age = []
for i in range(4):
    age.append(int(input(f"Enter Age of {i+1} Person: ")))
old = age[0]
for a in age:
    if a > old:
        old = a
print(f'The oldest is of age {old} and is the {age.index(old)+1} person.')