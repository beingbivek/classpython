#list
newlist = [1,2,3]
print(newlist)
newlist.insert(2,"ram")
print(newlist)
newlist.insert(1,"ram")
print(newlist)
t = 8,9
newlist.append((5,7))
print(newlist)
newlist[2] = 'hari'
print(newlist)
# del newlist[3]
newlist.remove('ram')
print(newlist)
newlist.pop()
print(newlist)
# copy command will generate new list in new memory with the same values
anotherlist = newlist.copy()
print(anotherlist)
print(id(anotherlist))
print(id(newlist))
anotherlist.extend(newlist)
print(anotherlist)
print(id(anotherlist))
print(newlist)
print(id(newlist))

#tuple
data = 1,2,3
print(data)