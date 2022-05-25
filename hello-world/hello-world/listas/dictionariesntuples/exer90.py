aluno = {}


aluno['Nome'] = str(input('Nome: '))
aluno['Nota'] = float(input('Nota: '))

if aluno['Nota'] <= 5:
    aluno['Situacao'] = 'Reprovado'
else:
    aluno['Situacao'] = 'Aprovado' 
print()
print(f'{aluno["Nome"]}, com a nota: {aluno["Nota"]} está {aluno["Situacao"]}')
    