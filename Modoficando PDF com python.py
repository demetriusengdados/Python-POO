#!/usr/bin/env python
# coding: utf-8

# In[4]:


import PyPDF2
import os


# In[ ]:


caminho_dos_pdfs = 'pdf'

novo_pdf = PyPDF2.PdfFileMerger()

for root, dirs, files in os.walk(caminho_dos_pdfs):
    for file in files:
        caminho_completo_arquivo = os.path.join(root, file)
        
        arquivo_pdf = open(caminho_completo_arquivo, 'rb')
        novo_pdf.append(arquivo_pdf)

with open(f'{caminho_dos_pdfs}/novo_arquivo.pdf', 'wb') as meu_novo_pdf:
    novo_pdf.write(meu_novo_pdf)


# In[ ]:


with open('pdf/novo_arquivo.pdf', 'rb') as arquivo_pdf:
    leitor = PyPDF2.PdfFileReader()
    num_paginas = leitot.getNumPages()
    
    for num_pagina in range(num_paginas):
        print(num_pagina)
        escrito = PyPdfFileWriter()
        pagina_atual = leitor.getPage(num_pagina)
        escritor.addPage(pagina_atual)
        
        with open(f'novos_pdfs/{num_pagina}.pdf', 'wb') as novo_pdf:
            escritor.write(novo_pdf)

