def divide(n1,n2):
    try:
        return n1/n2
    except Exception as e:
        print('LOG:', e)
        raise 

try:
    print(divide(2,0))
except ZeroDivisionError as erro:
    print( erro)