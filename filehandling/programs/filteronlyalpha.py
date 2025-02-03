# readlist = []
with open(r'D:\Bivek Study Files\Python Coding\filehandling\programs\softwarica.txt') as f:
    with open(r'D:\Bivek Study Files\Python Coding\filehandling\programs\python1.txt','w') as f1:
        alldata = f.read()
        for data in alldata:
            if not data.isdigit():
                f1.write(data)
                # readlist.append(data)
        # for cha in readlist:
        #     f1.write()
