class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} barks {sound}"




class GoldenRetriever(Dog):
    def speak(self, sound = "uau"):
        return super().speak(sound)


gr = GoldenRetriever("Pedro",11)

print(gr.speak())