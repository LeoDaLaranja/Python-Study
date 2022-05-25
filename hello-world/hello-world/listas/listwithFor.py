import random
numbers = [1, 3, 5]

print(5 in numbers)
print(8 in numbers)

print(5 not in numbers)
print(8 not in numbers)

print("\n----------//--------//--------//--------//--------//--------//--------//--------//--------//--------")

cities = ["Chicago","London","Tokyo"]

for city in cities:
    print(city)


print("\n----------//--------//--------//--------//--------//--------//--------//--------//--------//--------")

numbers = [42, 77, 16, 101, 23, 8, 4, 15, 55]
numbers.sort()

for number in numbers:
    if number>42:
        break
    print(number)

print("\n----------//--------//--------//--------//--------//--------//--------//--------//--------//--------")

numbers = []

while len(numbers) < 5:
    numbers.append(random.randint(1,100))

for number in numbers:
    print(number)
    if number >= 90:
        print("Found at least one number greater than 90 ")
        break
    else:
        print("No numbers greater than 90")
else:
    print("Complete")

print("\n----------//--------//--------//--------//--------//--------//--------//--------//--------//--------")

values = ["laptop", 7, "phone", 3, "dslr", 5]
equipment = []

for value in values:
  if isinstance(value, str) == False:
    continue
  equipment.append(value)

print(equipment)