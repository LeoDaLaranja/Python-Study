#How to define a class 
#If you don't have any code you can use pass to run the file wihtout any error 
class Dog:
    #Class attributes -> Have the same value for all class
    species = "Canis familiaris"
    #sets the initial state of the object by assigning the values of the object's properties 
    #init initializes each new instance of the class 
    def __init__(self, name, age, breed):
        self.name = name 
        self.age = age
        self.breed = breed
    #Instances Methods
    #it's better to use the _str_ to return information
    def __str__(self):
        return f'{self.name} is {self.age} years old'
    def speak(self,sound):
        return f'{self.name} says {sound}'

#child classes 
class JackRusselTerrier(Dog):
    def speak(self, sound = "Arf"):
        #use super() to acces the parent class from insede a method of a child class
        return super().speak(sound)
class Danchshund(Dog):
    pass
class Bulldog(Dog):
    pass

name = str(input("Name: "))
age = int(input("Age: "))
c1 = Dog(name,age)

print(c1)
print(c1.speak("Mopa"))

jc = JackRusselTerrier("Miles", 4)
bu = Bulldog("Buddy", 5)
jack = Danchshund("Jack", 6)

print(jc.species)
print(bu.name)
print(jack.speak("Auuu"))