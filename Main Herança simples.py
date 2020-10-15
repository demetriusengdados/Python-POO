from classes import *

"""
Associação - Usa \ Agregação - tem \ Composição - É dono \ Herança - É
"""

c1 = Cliente('Luiz', 45)
c1.falar()
c1.comprar()
print(c1.nome)

a1 = Aluno('Maria', 54)
a1.falar()
a1.estudar()
print(a1.nome)
