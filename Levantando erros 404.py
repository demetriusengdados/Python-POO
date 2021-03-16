#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from django.shorcurts import render
from django.http import Http404
from models import contato

def index(request):
    contatos = Contato.objects.all()
    return render(request, 'contatos/index.html', { 
        'contatos': contatos
    })

def ver_contato(request, contato_id):
    try:
        contato = Contato.objects.get(id=contato_id)
        return render(request, 'contato/ver_contato.html', {
            'contato': contato
        })
    except Contato.DoesNotExists as e:
        raise Http404()

