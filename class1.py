import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))
print(keyword.iskeyword('true'))
print(keyword.iskeyword('True'))
print(type(1+2j)) # Complex
a = 2
print(a.real)
print(a.imag)
print(type(a))
print(2 is 2)
a=1+3j
b=1+3j
print(a is b)

#String - Camel Case
firstName = 'ram'
lastName = 'kc'
print(id(firstName))
print(id(lastName))
print(firstName is lastName)

#Int - Pascal Case
NumberOne = 1
NumberTwo = 1
print(id(NumberOne))
print(id(NumberTwo))
print(NumberOne is NumberTwo)

#float - Snake Case
first_number = 1.0
second_number = 1.0
print(id(first_number))
print(id(second_number))
print(first_number is second_number)

#tuple - flat case
firstgroup = 'a','b'
lastgroup = ('a','b')
print(id(firstgroup))
print(id(lastgroup))
print(firstgroup is lastgroup)

#complex - upperflat case
IMAGINERYFIRST = 1+2j
IMAGINERYSECOND = 1+2j
print(id(IMAGINERYFIRST))
print(id(IMAGINERYSECOND))
print(IMAGINERYFIRST is IMAGINERYSECOND)

#set - camel snake case
first_Person = {'ram','kc'}
last_Person = {'ram','kc'}
print(id(first_Person))
print(id(last_Person))
print(first_Person is last_Person)

#dictionary - Pascal snake case
First_Pair = { "name":"Bivek", "surname":"Thapa"}
Second_Pair = { "name":"Bivek", "surname":"Thapa"}
print(id(First_Pair))
print(id(Second_Pair))
print(First_Pair is Second_Pair)

#List - Screeming snake case
FIRST_LIST = [1,2,3]
SECOND_LIST = [1,2,3]
print(id(FIRST_LIST))
print(id(SECOND_LIST))
print(FIRST_LIST is SECOND_LIST)