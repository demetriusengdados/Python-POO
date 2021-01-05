#!/usr/bin/env python
# coding: utf-8

# In[1]:


import subprocess


# In[13]:


proc = subprocess.run(
['ping', '127.0.0.1', '-c', '4'],
capture_output=True,
text=True
)
saida = proc.stdout
saida = saida.replace('icmp_seq', 'Demetrius')
print(saida)


# In[ ]:




