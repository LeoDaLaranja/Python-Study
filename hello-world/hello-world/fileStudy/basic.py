#open a file
file = open('..\..\basic.txt')

'''
When you're manipulating a file, there are two ways that you can use to ensure that a file is closed properly, even when encoutergin an erro.
'''

try:
    reader = file
finally:
    file.close()

#other way to close a file is to use the With statement

with open('basic.txt') as reader:
    print("Success")

'''
perhaps you must want to use the second positional argument, mode 
there are some of them here

r -> Open for reading
w -> Open for writing, truncating(overwriting) the file first
rb or wb -> Open on binary mode (read/write using byte data)

'''
print(type(file))

#Buffered binary file 

'''
A buffered binary file type is used for reading and writing binary files

open('abc.txt','rb')
or 
open('abc.txt','wb')
'''

reader = open('basic.txt','wb')
print(type(reader))

reader = open('basic.txt','rb')

#Raw files type 

'''
generally used as low-level building-block for binary and text streams
not tipically used 
'''

raw = file.open('basic.txt','rb',buffering = 0)
print(type(raw))

#Tips and tricks 

'''
__file__ attribute is a special attribute of modules, similar to __name__. It is:
The pathname of the file from which the module was loaded, if it was loaded from a file

'''

#Work with two files at the same time 

d_path = 'n1.txt'
d_r_path = 'n2.txt'

with open(d_path,'r') as reader, open (d_r_path,'w') as writer:
    n1 = reader.readlines()
    writer.writelines(reversed(n1))

#Creating your own context manager 

class my_file_reader():
    def __init__(self,file_path):
        self.__path = file_path
        self.__file_object = None


    def __enter__(self):
        self.__file_object = open(self.__path)
        return self

    def __exit__(self,type, val, tb):
        self.__file_object.close()

with my_file_reader('n1.txt') as reader:
#sei lá tu coloca alguma coisa aqui 
    pass



'''
Agora bora fazer um um PNG Reader
'''

class PngReader():
    #Every .png file contains this in the header. Use it to verify
    #the file is indeed a .png
    _expected_magic = b'\x89PNG\r\n\x1a\n'

    #b is used to specify the bytes in a string in python

    def __init__(self, file_path):
        # Ensure the file has the right extension

        if not file_path.endswith('.png'):
            raise NameError("File must be a '.png' extension ")
        self.__path = file_path
        self.__file_object = None

    def __enter__(self):
        self.__file_object = open(self.__path, 'rb')
        magic = self.__file_object.read(8)
        if magic != self._expected_magic:
            raise TypeError("The file is not a properly formatted .png file! ")
        
        return self

    def __exit__(self, type, val, tb):
        print ('n')
        