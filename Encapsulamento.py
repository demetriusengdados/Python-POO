"""
public = metodos e atributos que podem ser acessados dentro e fora da classe
protected = atributos de dentro da classe ou das filhas
private = atributos e metodos so podem acessados de dentro da classe
"""

class BaseDeDados:
  def __init__(self):
    self.dados = {}
    
    def inserir_clientes(self, id, nome):
     if 'cliente' not in self.dados:
       self.dados['clientes'] = {id: nome}
     else:
       self.dados['clientes'].update({id: nome})
    
    def lista_cliente(self):
      for id, nome in self.dados['clientes'].items():
        print(id, nome)
        
    def apaga_cliente(self, id):
      del self.dados['clientes'][id]
      
    
bd = BaseDeDados()
bd.inserir_cliente(1, 'Demetrius')
bd.inserir_cliente(2, 'Hilton')
bd.inserir_cliente(3, 'Joiane')
bd.inserir_cliente(4, 'Karine')
bd.inserir_cliente(5, 'José')
bd.apaga_cliente(2)
bd.lista_clientes()
print(bd.dados)
