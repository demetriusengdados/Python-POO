"""lista = ['A', 'B', 'C', 'D', 'E', 10.5]
print(lista)

string = 'ABCDE'
print(string)

l1 = [1,2,3,4,5]
l2 = [6,7,8,9,10]

l1.append(l2)
print(l1)
"""
#l2 = list(range(0, 100, 8))
#print(f'Os valores {l2} são pares')

secreto = 'Python'
digitadas = []
chances = 5 

while True:
    if chances < 0:
        print('Voce perdeu')
        
    letra = input('Digite uma letra: ')
    
    if len(letra) > 1:
        print('Ahhhh isso não vale, digite apenas uma letra')
        continue
    
    digitadas.append(letra)
    
    if letra in secreto:
        print(f'Uhul, a letra {letra} existe na palavra secreta')
    else:
        (f'Tente de novo essa {letra} não existe na palavra')
        digitadas.pop()
        
    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'
    if secreto_temporario == secreto:
        print(f'Que legal voce ganhou, a palavra era {secreto_temporario}')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')
        
    if letra not in secreto:
        chances -= 1
    