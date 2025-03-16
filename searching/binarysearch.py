arr = [1,5,6,11,16,17,22,25,26,66]
x = int(input('Enter your number: '))
low = mid = 0
high = len(arr) - 1
while low <= high:
    mid = (low + high) // 2
    if arr[mid] < x:
        low = mid + 1
    elif arr[mid] > x:
        high = mid - 1
    else:
        break
if arr[mid] == x:
    print('found it: ',mid,arr[mid])
else:
    print('Element Not found!')