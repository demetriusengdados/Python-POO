#!/usr/bin/env python
# coding: utf-8

# In[1]:


livros = list()
livros.append('Livro 1')
livros.append('Livro 2')
livros.append('Livro 3')
livros.append('Livro 4')
livros.append('Livro 5')
print(livros)
livro_removido = livros.pop()
print(livros, livro_removido)


# In[3]:


from collections import deque
fila = deque()
fila.append('João')
fila.append('Maria')
fila.append('Luiz Otávio')
fila.append('Marcos')
fila.append('José')
fila.popleft()
for nome in fila:
    print(nome)


# In[4]:


from collections import deque 
from time import sleep

fila = deque(maxlen=20)

for i in range(100):
    fila.append(i)
    sleep(1)
    print(fila)


# In[11]:


from collections import deque 
from time import sleep

fila = deque(maxlen=10)
fila.extend([10,20,30,40,50,60,70,80,90])
fila.rotate(1)
print(fila)


# In[ ]:




