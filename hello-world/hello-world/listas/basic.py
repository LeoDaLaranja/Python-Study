colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'brown']

print(colors)
print(type(colors))

print(colors[1])

print("\n----------//--------//--------//--------//--------//--------//--------//--------//--------//--------")

print("Use index to access individual elements")

colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'brown']

# print(colors)
# print(type(colors))

print(f'0-based indexing into the list ... second item: {colors[1]}')

print(f'Last item of the list: {colors[-1]}')
print("\n you can use negative index to access the last element in the list")
print(f'Next to last item in the list: {colors[-2]}')

print("\n----------//--------//--------//--------//--------//--------//--------//--------//--------//--------")

print("Create a slice ")
colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'brown']

# print(f'0-based indexing into the list ... second item: {colors[1]}')

# print(f'Last item of the list: {colors[-1]}')

# print(f'Next to last item in the list: {colors[-2]}')

print('\nPrint a SLICE, starting at index 2 and excluding index 5:')
print(colors[2:5])
print(type(colors[2:5]))

print('\nPrint a slice, starting at index 0 to index 3:')
print(colors[:3])

print('\nPrint a slice, starting a index 4 to the end of the list:')
print(colors[4:])

print('\nPrint a slice, from the 4th from the end (but not the last item):')
print(colors[-4:-1])

print("\n----------//--------//--------//--------//--------//--------//--------//--------//--------//--------")

print("The reverse and the sort form of a list ")

colors.reverse()
print(colors)

colors.sort()
print(colors)

print("\n----------//--------//--------//--------//--------//--------//--------//--------//--------//--------")
print("Treat the list like a queue")

'''
We can use the list to make a queue, fila in portuguese, with the function pop()
It's possible to remove the first item with the index 0 and the last with -1
In other words, its possible to make de Fist in, first out (FIFO) and the last in, first out(LIFO).
'''

print(colors)

color = colors.pop(0)
print('popped',color)

print(colors)

print("\n----------//--------//--------//--------//--------//--------//--------//--------//--------//--------")

print(colors)

colors.append('black')
colors.append('white')

colors.remove('yellow')
colors.remove('orange')

print(colors)

'''
append == insert
remove == remove asuhaushahu
You cant remove a item that doesnt exist in the list!!!'''

print("\n----------//--------//--------//--------//--------//--------//--------//--------//--------//--------")

print("Combine a list with an existing list ")

new_colors = ['lime', 'gray']
colors.extend(new_colors)

print(colors)

print("\n----------//--------//--------//--------//--------//--------//--------//--------//--------//--------")

print(colors)
colors.clear()
print(colors)

print("\n----------//--------//--------//--------//--------//--------//--------//--------//--------//--------")
