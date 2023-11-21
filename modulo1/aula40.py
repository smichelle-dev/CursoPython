perguntas = [
    {
        'Pergunta':'Quanto é 2+2',
        'Opções':['1','2','3','4','5'],
        'Resposta':'4',
    },

     {
        'Pergunta':'Quanto é 5*5',
        'Opções':['25','65','30','80','58'],
        'Resposta':'25',
    },

     {
        'Pergunta':'Quanto é 10/2',
        'Opções':['4','5','2','1','5'],
        'Resposta':'5',
    },
 
]

for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

for i, opcao in  enumerate(pergunta['Opções']):
   print(opcao)

print()