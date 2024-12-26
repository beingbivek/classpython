bad_chars = [';', ':', '!', "*", " "]
string = "py;th* o:n ! ;py * t*h:o !n"
newstring = ''

for i in string:
    for j in bad_chars:
        if i == j:
            break
    else:
        newstring += i

    # print(newstring + "inside")

# print(newstring + 'out')
            
print(newstring)