from time import sleep

counts = dict()
names = ['Leo','Leo','Leo2','Leo2','Leo4']

#conta os valores
'''for name in names:
    if name not in counts:
        counts[name] = 1 
    else: 
        counts[name] = counts[name] + 1 
print(counts)
'''
#metodo get 

'''
The pattern of checking if a key is a already in a dictionary 
and assuming a default value if the key is not there and no traceback 
'''

#Assim ficaria com o uso do get 
print('Com o metodo get')
for name in names:
    counts[name] = counts.get(name,0) + 1 
print('Sim, ao rodar o código de cima junto com esse ele retorna o valor em dobro, já que você está adicionando mais valores')
print(counts)
sleep(2)
#lendo e slipando linhas 
words_count = dict()
line = input('Enter a line of code: ')
words = line.split()

print('Words: ', words)

print('Counting...')

for word in words:
    words_count[word] = words_count.get(word,0)+1

print('Counts ',words_count)
sleep(2)
print('Printando as chaves e valores')
#counting 
for key in counts:
    print(key, counts[key])
print(counts.items())
sleep(2)

print('Printando com key e value em um for')

for k,v in counts.items():
    print('Key ', k, 'Values', v)
