def varios(*a, **n):
    for c in a:
        print(c)
    for c in n:
        print(c)
list = [1,2,23,4,55,6]
nomes = ['Leo','zin','Tpx']
varios(list,nomes)