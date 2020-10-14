class Produto:
  def __init__(self, nome, preço):
    self.nome = nome
    self.preço = preço
    
    def desconto(self, percentual):
      self.preço = self.preço - (self.preço * (percentual / 100))
      
    # Metodo Getter
    @property
    def preço(self):
      return self._preço
    
    
    # Metodo Setter
    @preço.setter
    def preço(self, valor):
      if isinstance(valor, str):
        valor = float(valor.replace('R$', ''))
      self._preço = valor
      
      
p1 = Produto('Camiseta', 50)
p1.desconto(10)
print(p1.preço)

p2 = Produto('Caneca', 'R$15')
p2.desconto(10)
print(p2.preço)
