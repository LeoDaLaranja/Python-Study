print(type('7'))
print(type(7))
print(type(7.1))

print('\n --------//-----------//---------//--------')
print("isistance()")

print(isinstance('7',str))
print(isinstance(7,int))
print(isinstance(7.1,float))

print(isinstance(7,str))
print(isinstance('7',int))
print(isinstance('7.1',float))

print("Float para comparar")
n = float(input())
if isinstance(n,str):
    print("É verdade ")
else:
    print("Não é ")