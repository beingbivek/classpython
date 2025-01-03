givenstring = "py;th* o:n ! ;py * t*h:o !n"
bad_chars = [';', ':', '!', "*",' ']
newstirng = ''
i = 0
while i < len(givenstring):
    j = 0
    check = False
    while j < len(bad_chars):
        if givenstring[i] == bad_chars[j]:
            check = True
            break
        j += 1
    if check == False:
        newstirng += givenstring[i]
    i += 1

print(newstirng)