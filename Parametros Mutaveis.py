def lista_de_clientes(clientes_iteravel, lista=None):
  if lista is None:
    lista = []
  lista.extend(clientes_iteravel)
  return lista


clientes1 = lista_de_clientes(['João', 'Maria', 'Eduardo'])
clientes2 = lista_de_clientes(['Marcos', 'Jonas', 'Zico'])
clientes3 = lista_de_clientes(['José', 'Adriano', 'Thiago'])

print(clientes1)
print(clientes2)
print(clientes3)