from typing import BinaryIO


file = input('File name: ')
file = f'.\listas\dictionariesntuples\{file}'
handle = open(file)

counts = dict()

for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) +1

bigCount = None
bigWord = None

for word, count in counts.items():
    if bigCount is None or count> bigCount:
        bigCount = count 
        bigWord = word

print(bigCount,'', bigWord)