pergunta = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2 ? ',
        'respostas': {'a': '1', 'b': '4', 'c': '5',},
        'resposta certa': 'b',
    },

        'Pergunta 2': {
            'pergunta': 'Quanto é 3 * 2 ? ',
            'respostas': {'a': '4', 'b':'10', 'c':'6',},
            'resposta certa': 'c',
        },
}

for pk, pv in pergunta.items():
  print(f"{pk}: {pv['pergunta']}")