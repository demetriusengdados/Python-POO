from classes import *

"""
Associação - Usa \ Agregação - tem \ Composição - É dono \ Herança - É
"""

c1 = Cliente('Luiz', 45)
c1.falar()
c1.comprar()
print(c1.nome)

print()

c2 = ClieneteVIP('Rose', 25, 'Miranda')
c2.falar()
