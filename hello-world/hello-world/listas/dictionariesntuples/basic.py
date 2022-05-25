'''
Dictionaries differ from lists by the way in how elements are accessed:
    Lists elements are accessed by their position in the list, via indexing
    Dictionary elements are accessed via values

'''

#Defining the dictionary 
MLB_team = {
     'Colorado': 'Rockies',
     'Boston':'Red Sox'

 }
print(MLB_team)

'''
you can also construct a dictionary with the built-in dict()

MLB_team = (
    [
        ('key','value')
    ]
)
if the key values are simple values, they can be specified as keyword arguments 

    Colorado = 'Rockies'
'''
bracke_team = dict([
    ('Minnesota', 'Twins'),
    ('Milwaukee', 'Brewers')
])

print(bracke_team)

# Accessing values 

'''
A value is retrieved  from a dictionary by specified its corresponding key in square brackets 
'''

print(MLB_team['Boston'])

'''
A given key can appear in dictionary only once. Duplicated keys are not allowed 
A dictionary key must be of a tipe that is immutable 
A tuple can also be a dictionary, because tuples are immutable 

However, neither a list nor another dictionary can serve as a dictionary key, because the are mutable 
'''

print(len(MLB_team))
print(bracke_team.get('Milwaukee'))

# d.items rerturns a list of tuples containing the key-value pair in bracke_team
#the first item in each tuple is the key and the second is the key value


print(bracke_team.items())