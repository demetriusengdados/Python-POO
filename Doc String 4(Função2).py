variavel_1 = 'valor1'

def soma(x, y):
  """
  Soma x e y
  
  :param x: Primeiro Numero
  :type x: int ou float
  :param y: Segundo Numero 
  :type y: int ou float
  
  return:  A soma entre x e y
  :rtype: int or float
  """
  return x + y
  
  
  
def multiplica(x, y, z=None):
  """
  soma x,y,z
   multiplica x, y, z. O programador por omitir a variavel z caso não tenha 
   necessidade de usa-la
  :param x: Primeiro Numero
  :type x: int ou float
  :param y: Segundo Numero 
  :type y: int ou float
  
  return:  A soma entre x e y
  :rtype: int or float
  """
  
  if z:
    return x * y
  else:
    x * y * z
    
variavel_2 = 'valor 2'
variavel_3 = 'valor 3'
variavel_4 = 'valor 4'
