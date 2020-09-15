"""from types import GeneratorType

variavel = ( ( x, y)for x, y in zip('Alo', 'Alo'))

print(list(variavel))"""


from itertools import count

cont = count(step=0.1)

for valor in cont:
    print(round(valor, 2))
    
    if valor >= 50:
        break