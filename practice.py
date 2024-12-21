a = r'python'
b = a.maketrans('non','cbd')
print(b)
print(a.translate(b))

print(a.replace('pth','b'))
print(a.startswith(''))

print('python\tprog')
print('python\tprog'.expandtabs(tabsize=15))
print('python\rspi\ba')
print('pt' in a)
print(f'{0}{0}')
# print(f'{}'.format(a))

c = 'programming'
print(a[-15::-2])

d = 99
print(d.isdigit())