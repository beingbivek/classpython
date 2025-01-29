# abcaas dbcad dsadsa
# user_input = input('Enter a long string: ')
user_input = 'abcaasdbcaddsadsa'
listofrepeatingchar = []
repeatingchar = ''
p = ''
for i in user_input:
    if i != p:
        repeatingchar += i
    else:
        listofrepeatingchar.append(repeatingchar)
        repeatingchar = ''
    p = i
print('largest  char: ',max(listofrepeatingchar))