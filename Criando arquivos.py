"""file = open ('abc.txt', 'w+')
file.write('linha 1\n')
file.write('linha 2\n')
file.write('linha 3\n')
file.write('linha 4\n')
file.write('linha 5\n')

file.seek(0, 0)
print('Lendo Linhas')
print(file.read())
print('###############')

file.seek(0, 0)
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())

print('###############')

file.seek(0, 0)
for linha in file.readlines():
    print(linha, end='')

file.close()
"""

