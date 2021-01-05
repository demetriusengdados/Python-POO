#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from time import sleep 
from threading import Thread
from threading import lock
class MeuThread(Thread):
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo
        super().__init__()
        
    def run(self):
        sleep(self.tempo)
        print(self.texto)
        
t1 = MeuThread('Thread 1', 5)
t1.start()

t2 = MeuThread('Thread 2', 10)
t2.start()

t3 = MeuThread('Thread 3', 15)
t3.start()

t4 = MeuThread('Thread 4', 20)
t4.start()

t5 = MeuThread('Thread 5', 25)
t5.start()


for i in range(25):
    print(i)
    sleep(1)
  
def vai_demorar(tempo):
    sleep(tempo)
    print(texto)


t1 = Thread(target=vai_demorar, args=('Olá mundo!', 5))
t1.start()

t2 = Thread(target=vai_demorar, args=('Entre com seu usuário!', 10))
t2.start()

t3 = Thread(target=vai_demorar, args=('Entre com sua senha!', 15))
t3.start()

t4 = Thread(target=vai_demorar, args=('Bem vindo!', 20))
t4.start()

t5 = Thread(target=vai_demorar, args=('Vamos começar!', 25))
t5.start()

for i in range(25):
    print(i)
    sleep(.5)


# In[ ]:


def vai_demorar(tempo):
    sleep(tempo)
    print(texto)


t1 = Thread(target=vai_demorar, args=('Olá mundo!', 5))
t1.start()
t1.join()

while t1.is_alive():
    print('Esperando execução da Thread')
    sleep(2)
    
print('Thread executada com sucesso')

class Ingressos:
    def __init__(self, estoque):
        self.estoque = estoque
    
    def comprar(self, quantidade):
        self.lock.acquire()
        if self.estoque < quantidade:
            print('Não temos ingressos suficientes')
            sel.lock.release()
            return
        print(f'Voce comprou {quantidade} ingressos. 
              Ainda temos {self.estoque}')
        self.estoque -= quantidade
        self.acquire.release()

if __name__ == '__main__':
    ingressos = Ingressos(10)
    ingressos.comprar(1)
    ingressos.comprar(1)
    ingressos.comprar(1)
    ingressos.comprar(1)
    ingressos.comprar(1)
    
    for i in range(1, 20):
        t = Thread(target=ingressos.comprar, args=(i,))
        t.start()
    
    print(ingressos.estoque)

