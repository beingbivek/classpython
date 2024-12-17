a = "pyThoN"
print(a.swapcase())
a = "python"
print(a.replace("p","Z"))
a = "python"
print(a.replace("py","Z")) # replaces both 
a = "python"
print(a.replace("x","Z")) # when character is not found it returns a as it is"
# ASCII Codes: a-z = 97-122, A-Z = 65-90, 0-9 = 48-57
a = "python"
b = a.maketrans("p","z")
print(a.translate(b)) # it only
b = a.maketrans("PXK","WXK")
print(b) # it only
print(a.translate(b)) # it only

left = a.ljust(7,"*")
right = a.rjust(7,"*")
print(left,right)
#OR
b = "*" + a[:]
print(b)

a = 'abc'
b = a.maketrans('abc','efg')
print(b)
print(a.translate(b))

print(a.zfill(8)) # adds 0's to left

print(a.startswith("ab"))
print(a.endswith("")) 
# in above both case if empty strings are given then it returns true

# in below case, only aplhabets are ture, special characters are false even spcaes
a = 'python'
print(a.isalpha()) 
print(a.isidentifier())
print(a.isprintable())
a = '\n'
print(a.isspace()) # only spaces and non printable characters are true

a = 'python'
# print(a["p"]) # using index
# Slicing
print(a[1:6])
print(a[0:6:2]) # start:end:step
print(a[:])
print(a[:3])

print("----------")
num = '1122aasv'
print(num.maketrans("aa","12"))
print(num.translate(num.maketrans("2a","11")))