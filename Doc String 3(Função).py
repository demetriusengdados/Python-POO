"""Documetação oficial"""
variavel_1 = 'valor 1'

def soma(x, y):
  #soma x e y
  return x + y


def multiplica(x, y, z=None):
  """Soma x, y, z
  Multiplica x, y, z o programador por omitir a variavel z caso não tenha
  necessidade de usa-la
  """
  if z:
    return x * y
  else:
    return x * y * z
  

variavel_2 = 'valor 2'
variavel_3 = 'valor 3'
variavel_4 = 'valor 4'