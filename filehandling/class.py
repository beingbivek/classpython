# f = open(r'D:\Bivek Study Files\Python Coding\filehandling\abc.txt')
# c = f.read()
# f1 = open(r'D:\Bivek Study Files\Python Coding\filehandling\python.txt','w')
# f1.write(c)
# f.close()
# f1.close()

# f = open(r'D:\Bivek Study Files\Python Coding\filehandling\abc.txt','w')
# n = f.write('\n12345\t')
# print(n)
# f.close()
# print("---------------")

# f = open(r'D:\Bivek Study Files\Python Coding\filehandling\python.txt','r')
# data = f.readlines()
# # data2 = f.readline()
# # print(data,data2,end='')
# print(data)
# for i in data:
#     print(i,end='')
# f.close()

# print(f.tell())
# data = f.read(5)
# print(data)
# print(f.tell())
# data = f.read(3)
# print(data)
# print(f.tell())
# f.seek(3)
# print(f.tell())

# with open(r"D:\Bivek Study Files\Python Coding\filehandling\python.txt") as f:
#     data = f.read()
#     print(f.closed)
#     print(data)
# print(f.closed)

import pickle

# # using dump-load
# # pickling

# f = open(r'D:\Bivek Study Files\Python Coding\filehandling\picklefile.txt','wb')
# dct = {'1':'Ram','2':'Hari'}
# pickle.dump(dct,f)
# f.close()

# # unpickling
# f = open(r'D:\Bivek Study Files\Python Coding\filehandling\picklefile.txt','rb')
# d = pickle.load(f)
# print(d)
# f.close()

# using dumps-loads
lst = [1,2,3,4,5]
p = pickle.dumps(lst)
print(p)
d = pickle.loads(p)
print(d)