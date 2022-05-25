#sorting lists of tuples 

d = {'c': 10 , 'x': 4, 'a': 6}

print(d.items())

print('Printing Sorted Items: ')

for k,v in sorted(d.items()):
    print('key',k, 'value', v)

fhand = open('.\listas\dictionariesntuples\mopa.txt')
counts = dict()

for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0)+1

lst = list()
for k,v in counts.items():
    newtup = (v,k)
    lst.append(newtup)

lst = sorted(lst, reverse=True)

for v, k in lst[:10]:
    print(k,v)