"""texto = 'python e uma linguagem simples'

for n, in enumerate(texto):
    print(n)
    

for n in range (0, 100, 8):
    print(n)
print('-' * 100)
    
for n in range(100):
    if n % 8 == 0:
        print(n)
       """

texto = 'Python'
nova_string = ''

for letra in texto:
    if letra == 't':
        nova_strig = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
        break
    else:
        nova_string += letra
        
print(nova_string)
