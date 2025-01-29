user_num = int(input('Enter a no: '))

def mtable(num):
    for i in range(1,11):
        print(num,"*",i,"=",num*i)


mtable(user_num)