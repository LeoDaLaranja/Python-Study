num = ('zero','um','dois','tres','quatro')

for c in range(len(num)):
    n = int(input('N: '))
    print(n)

    for c, i in enumerate(num):
        if n == c:
            print(i)
