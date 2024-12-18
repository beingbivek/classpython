age = []
for i in range(4):
    age.append(int(input(f"Enter Age of {i+1} Person: ")))
    
# age.append(int(input("Enter Age of Second Person: ")))
# age.append(int(input("Enter Age of Third Person: ")))
# age.append(int(input("Enter Age of Fourth Person: ")))
young = age[0]
for a in age:
    if a < young:
        young = a
print(f'The youngest is of age {young} and is the {age.index(young)+1} person.')

# Simpler Method
first = int(input("Enter age of First Person: "))
second = int(input("Enter age of Second Person: "))
third = int(input("Enter age of Third Person: "))
fourth = int(input("Enter age of Fourth Person: "))

if first <= second and first <= third and first <= fourth:
    print("First person is the Youngest")
elif second <= third and second <= fourth and second <= first:
    print("Second person is the Youngest")
elif third <= second and third <= first and third <= fourth:
    print("Third person is the Youngest")
else:
    print("Fourth is the Youngest")
