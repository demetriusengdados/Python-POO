"""def olá_Mundo():
    return 'Olá Mundo'

def mestre(funcao):
    return funcao()

executando = mestre(olá_Mundo)
print(executando)
"""

def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def fala_oi(nome):
    return f'Oi {nome}'

def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'

executando = mestre(fala_oi, 'Demetrius')
executando2 = mestre(saudacao, 'Demetrius', saudacao='Bom dia')
print(executando)
print(executando2)
