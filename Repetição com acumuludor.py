contador = 0
acumulador = 1
while contador <= 100:
    print(contador, acumulador)
    if contador > 50:
        break
    acumulador = acumulador + contador
    contador += 1
else:
    print('Chegamos ao final')
print('Chegamos ao final')
        
