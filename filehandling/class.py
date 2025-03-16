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

filelocation = r"D:\Bivek Study Files\Python Coding\filehandling\student.txt"

# with open(r"D:\Bivek Study Files\Python Coding\filehandling\python.txt") as f:
#     data = f.read()
#     print(f.closed)
#     print(data)
# print(f.closed)

# f=open(r'D:\Bivek Study Files\Python Coding\filehandling\student.txt',mode='r')
# print("File Name: ",f.name)
# print("File Mode: ",f.mode)
# print("File Readable: ",f.readable())
# print("File Writable: ",f.writable()) 
# print("File Closed: ",f.closed)
# f.close()
# print("File Closed: ",f.closed)


# f = open(r"D:\Bivek Study Files\Python Coding\filehandling\student.txt", mode='a')
# lst=['ram','shyam\n','hari\n','gita\n']
# f.writelines(lst)
# f.close()
# print("Success")

# f=open('sand.txt',mode='x')
# print(f.writable())
# f.close()

# f=open(filelocation,mode='r')
# print(f.tell())
# data=f.read(5)
# print(data)
# print(f.tell())
# data1=f.read(3) 
# print(data1)
# print (f.tell())


# f=open(filelocation,mode='r')
# print(f.tell())
# f.seek(2)
# print(f.tell())
# data=f.read(5) 
# print(data)
# f.seek(2)
# print(f.tell())
# data=f.read() 
# print(data)

# Binary File
# Reading the image file in binary mode
# with open(r'D:\Bivek Study Files\Python Coding\tkinterclass\hill.png', 'rb') as source_file:
#     # Read the binary data from the source image
#     image_data = source_file.read()

# # Writing the binary data to a new file
# with open('copy_image.jpg', 'wb') as destination_file:
#     # Write the binary data to the destination image
#     destination_file.write(image_data)

# import pickle

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
# lst = [1,2,3,4,5]
# p = pickle.dumps(lst)
# print(p)
# d = pickle.loads(p)
# print(d)