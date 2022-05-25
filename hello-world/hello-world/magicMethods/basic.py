#Magic Methods or Dunder Methods 

'''
Are the special methods that start and end with the double underscores; They are also called dunder methoods.

Magic Methods are not meant to be invoked directly by you, but the invocation happens internall from the class
on a certain action.
For example, when you sadd two numbers using the + operator, internally, the __add__() method will be called.

'''

#Test
num = 10 
 

print(num.__add__(5))

'''
Magic methods are most frequently used to define overloaded behaviours of predefined operators in Python. 
numeric objects must be used along with operators like +,-,*,/ etc.
The + operator is also ddefined as a concatenation operator in string, list and tuple classes. 
We can say that the + operator is overloaded.
'''
print('')
num = 11+5
print(num)
print('')
num = 'Leo'+'nardo'
print(num)
print('')
'''
See? the + operator is overloaded

In order to make the overloaded behaviour available in your own custom class, the corresponding magic method should be overriden

For example, in order to use the + operator with objects of a user-defined class, it should include the __add__() method
'''

# Implementation 

## __new__() method 
'''
the __new__() magic method is implicitly called before the __init__() method
Returns a new object,which is then initialized by __init__()
'''

class Employee:
        def __new__(cls):
            print("__new__ magic method is called")
            inst = object.__new__(cls)
            return inst
        def __init__(self):
            print("__init__ magic method is called")
            self.name = "Leo"
# It will produce an outup when you create an instance of the Employee class;

emp = Employee()
#Thus, the __new__() mehtod is called before the __init__() method 

# __str__() method 

'''
It is overridden to return a printable string representation of any user defined class. 

str() -> returns a string from the object parameter. -> str(12) = '12'

When invoked, it calls the __str__() method in the class
'''
print('')
num = 12 
print(str(num))
print('')
#This is equivalent to 
print(int.__str__(num))
print('')
'''
Now, let's override the __str__() method in the employee class to return a string representation of its object 



'''
class Employee:
    def __init__(self):
        self.name = 'Leo'
        self.salary = 1000
    def __str__(self):
        return 'name='+self.name+' salary=$'+str(self.salary)

e1 = Employee()
print(e1)

# __add__ method 

class distance:
    def __init__(self,x = None, y = None):
        self.ft = x
        self.inch = y
    def __add__(self,x):
        temp = distance()
        temp.ft = self.ft+x.ft
        temp.inch = self.inch+x.inch
        if temp.inch>=12:
            temp.ft+=1
            temp.inch-=12
            return temp
    def __str__(self):
        return 'ft: '+str(self.ft)+' inch:'+str(self.inch)

d1 = distance(3,10)
d2 = distance(4,4)

print(f'd1 = {d1} d2 ={d2}')
d3 = d1+d2
print(d3)

#__ge__() method 
'''
Is added in the distance class to overload the >= operator 
'''

class distance:
    def __init__(self,x = None, y = None):
        self.ft = x
        self.inch = y
    def __ge__(self, x):
        val1 = self.ft*12+self.inch
        val2=x.ft*12+x.inch
        if val1>=val2:
            return True
        else: 
            return False
#This method get invoked when the >= operator is used and returns True or False Accordingly, the appropriate message can be displayed 
print('')
d1 = distance(2,1)
d2 = distance(4,10)
print(d1>=d2)
