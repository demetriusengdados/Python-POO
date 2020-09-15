#lista =  [0,1,2,3,4,5,6,7,8,9,10]
#lista = iter(lista)
#print(next(lista))
#print(next(lista))
#print(next(lista))
#print(next(lista))
#print(next(lista))
#print(next(lista))
#print(next(lista))
#print(next(lista))
#print(next(lista))
#print(next(lista))

#print(hasattr(lista, '__next__'))

"""import sys 
lista = list (range(10))
print(sys.getsizeof(lista))"""

import sys 
import time

def gera():
    r = []
    for n in range(100):
        yield n
        time.sleep(0.1)
    return r 

g = gera()
for v in g:
    print(v)
    