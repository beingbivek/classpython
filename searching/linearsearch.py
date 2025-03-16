arr = [1,23,34,1223,432,23,2332,34,123,23345,5,3242,3423,323,235,46,45]
x = int(input("Enter a number: "))
index = 0
for i in arr:
    if i == x:
        index = arr.index(i)
        print(index)
    else:
        index = -1
if index != -1:
    print('found value at index = ',index)
else:
    print('Can\'t find')
        