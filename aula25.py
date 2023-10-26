#tipos multaveis 

lista_1 = ['caneta', 'papel', 'tesoura', 'caderno']
#lista_2 =  ['prato', 'talheres','copos', 'bacia']

lista_2 =lista_1.copy()

lista_1[2]= 'chaveiro'
print(lista_1)
print(lista_2)

for nome in lista_1:
    print(nome, type(nome))

    