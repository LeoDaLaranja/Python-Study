'''
.read(size=-1) read based on the number of size bytes. If no argument is passed or none or -1 is passed, then the entire file is read.
.readline(size=-1) reads at most size number of characters from the line.-> continues to the end of the line and then wraps back around. -> if no arguments is passed or none or -1, the the entire line is read
.readlines() reads the remainig lines from the file object and returns them as a list.
'''
file = open('C:\Users\leonardo.laranjeira\hello-world\fileStudy\basic.txt')

print(file.read())
