a = 'abc\rprogramming'
print(a)
a = 'abc\nprogramming'
print(a)
a = 'abc\bprogramming'
print(a)
a = 'abc\'s programming'
print(a)
a = 'abc\tprogramming'.expandtabs(tabsize=8)
print(a)
a = 'abc\tprogramming'
print(a)
print('C:Users\\Python')
a='pYtHOn pRogRam'
print(a.upper())
print(a.lower())
print(a.capitalize())
print(a.title())
print(a.center(19,"*"))
print(a.center(15,"*"))
print(a.center(10,"*"))
print(a.startswith('o'))
print(a.ljust(16,'*'))
print(a.rjust(20,'*'))
print(a.find('n'))
print(a[5])
print(a[-4])
print(a.rfind('p'))
print(a.find('p'))
print(a.index('p'))
print(a.rindex('p'))

#difference between find and index
# print(a.find('w'))
# print(a.rfind('w'))
# print(a.index('w'))
# print(a.rindex('w'))

print("-----")
a='python'
b = a.rfind('t')
print(b)
c = b - len(a)
print(c)