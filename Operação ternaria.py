idade = input('Qual sua idade: ')
if not idade.isnumeric():
    print('Voce precisa apenas numeros.')
else:
    idade = int(idade)
    e_de_maior = ( idade >= 18)
    msg = 'Pode acessar' if e_de_maior else 'Não pode acessar.'
    
    print(msg)
    