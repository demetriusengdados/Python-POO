#d1 = dict(chave1= 'Valor da chave', chave2 ='Chave com outro valor')
#print(d1)

d1 = {
      'str': 'valor',
      123: 'Outro Valor',
      (1,2,3,4): 'Tupla',
      }

d1['str'] = 'Agora ela existe'

if d1.get('nova_chave') is not None:
    print(d1.get('nova_chave'))
    
print(123)



