def my_s(*args):
    result =0
    #Iterating over the python args tuple
    for x in args:
        result +=x  
    return result 

print(my_s(1,2,3))

# The args is just a name, but you can pass any name you want 

'''
Using the **kwars variable in function Definitions
'''
print('')
print("Using **kwargs")


def concatenate(**kwagrs):
    result = ""
    # Iterating over the Python kwagrs dictionary 
    for arg in kwagrs.values():
        result +=arg
    return result 

print(concatenate(a="Real",b="Python", c="Is", d="Great", e="!"))

#Unpacking with the Asterisk Operators 
print('')
print("Unpacking with the Asterisk Operators ")

'''
def my_sum(a,b,c):
    print(a+b+c)

my_list = [1,2,3]
my_sum(*my_list)
'''

def my_sum(*args):
    result = 0
    for x in args:
        result +=x 
    return result  

list1 = [1,2,3]
list2 = [4, 5]
list3 = [6, 7, 8, 9]

print(my_sum(*list1, *list2, *list3))

print('')
print('Spliting a list into three different parts')
my_list =[1,2,3,4,5,6,]

a, *b,c = my_list 
print(a)
print(b)
print(c)
print('')

print('')
print("You can split the items of any iterable object")
print('Its very useful if you need to merge two lists')
my_first_list = [1, 2, 3]
my_second_list = [4, 5, 6]
my_merged_list = [*my_first_list, *my_second_list]

print(my_merged_list)
print('')

print('You can even merger two different dictionaries by using the unpacking operator **')

my_first_dict = {"A": 1, "B": 2}
my_second_dict = {"C": 3, "D": 4}
my_merged_dict = {**my_first_dict, **my_second_dict}

print(my_merged_dict)

print('')
print('Remember that the * operator works on any iterable object, it can also unpack a string')

a = [*"RealPython"]
print(a)

#In python, strings are itrable objeects, so * will unpack it and place al individual values in a list a:

print('')
print('But you should use keep in mind the seventh rule of The Zen of Python, Readibility Counts')

*a, ="RealPython"
print(a)
'''
There’s the unpacking operator *, followed by a variable, a comma, and an assignment. That’s a lot packed into one line! 
In fact, this code is no different from the previous example.
It just takes the string RealPython and assigns all the items to the new list a,
thanks to the unpacking operator *.

The comma after the a does the trick. When you use the unpacking operator with variable assignment, 
Python requires that your resulting variable is either a list or a tuple. 
With the trailing comma, you have defined a tuple with only one named variable, a, which is the list

'''