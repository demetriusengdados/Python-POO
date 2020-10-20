"""Documentação simples"""
class MinhaClasse:
  atributo = 1
  atributo2 = 'valor'
  
  def __init__(self, texto):
    """ Inicializa os dados
    
    :param texto: o texto da classe
    :type texto: str
    """
    self.texto = texto
    self.exibe_texto(texto)
    
    
  @staticmethod
  def exibe_texto(texto):
    
    """ Metodo que exibe um texto de 100 caracteres na tela
    :param texto: Um texto de 100 caracteres
    :type texto: str
    
    :return: o texto de 100 caracteres
    :rtype: str
    
    :raises ValueError: Se o texto tiver mais que 100 caracteres
    :raises TypeError: Se o texto não for uma string
    """
    if not isinstance(texto, str):
      raise TypeError('Texto precisa ser uma string')
    
    if len(texto) > 100:
      raise ValueError('Texto precisa ter 100 caracteres ou menos')
      
    return texto
  