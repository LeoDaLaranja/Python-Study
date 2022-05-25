from typing import Counter


medicine = 'Coughussin'
dosage = 5
duration = 4.5

instruction = '{} - Take {} ML by mouth every {} hours '.format(medicine, dosage, duration)
print(instruction)

instruction = '{2} - Take {1} ML by mouth every {0} hours '.format(medicine, dosage, duration)
print(instruction)

instructions = '{medicine} - Take {dosage} ML by mouth every {duration} hours'.format(medicine = 'Sneezergen', dosage = 10, duration = 6)

print(instructions)

print('\n----------//-----------//------------//------')

name = 'World'
message  = f'Hello, {name}'
print(message)

count = 10 
value = 3.14 

message = f'Count to {count}. Multiply by {value}'
print(message)

print("\n----------//---------//------------//-------")

width = 5
height  = 10
print(f'The perimeter is {(2*width)+(2*height)} and the area is {width * height}.')


print('\n----------//----------//------------//-------')

value = 'hi'

print(f'.{value:<25}.')
print(f'.{value:>25}.')
print(f'.{value:^25}.')
print(f'.{value:-^25}.')