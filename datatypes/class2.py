# a = 1,2,3,4
# b = a[0:2]+'ram'
# print(b)

# a = {1,'ram',8.12,'shaym'}
# print(a)
# a.pop()
# print(a)

a = {'ram' : 1}
# k = a.values()
# l = list(k)
# print(type(l))
# b = a.popitem()
# c = {b[0].upper():b[1]}
# print(c)

a.pop('ram')
a['RAM'] = 1
print(a)