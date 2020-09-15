from itertools import combinations, permutations, product
pessoas = ['Luiz', 'Andre', 'Eduardo', 'Leticia', 'Fabiricio', 'Rose']

for grupo in combinations(pessoas, 4):
    print(grupo)
    