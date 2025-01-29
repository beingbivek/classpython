def mul(num):
    m = 1
    for i in num:
        m *= i
    return m

numlist=[4,5,3,2]
product = mul(numlist)
print('Product is: ',product)