# add (adiciona), update(atualiza), clear, discard
# union | (une)
#intesection  & (todos os elementos presentes nos dois sets )
#difference - (elementos apenas no set da esquerda)
#symetric_difference ^ (Elementos que estão nos dois sets, mas não em ambos)
#é parecido como um dicionário, porém não pode ser iniciado com {}
#porque o python interpreta como um dict
s1 = set()

s1.add(1)
s1.add(2)
s1.add((1,2,3))

print(s1)
s1.discard((1,2,3))
print(s1)

s1.update('Python')
print(s1)

