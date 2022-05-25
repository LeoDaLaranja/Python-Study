class Car():
    def __init__(self,color,mileage):
        self.color = color
        self.mileage = mileage
    
    #instance methods
    def __str__(self):
        return f'the {self.color} car has {self.mileage} miles'
c1 = Car("Blue", 20.000)
c2 = Car("Red", 30.000)
for car in (c1,c2):
    print(f"The {car.color} car has {car.mileage:,} miles")