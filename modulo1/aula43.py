lista_precos=[10000,200,100,50,20000]

imposto=[]
for preco in lista_precos:
    if preco > 1000:
        imposto.append(preco*0.5)
        print(imposto)

imposto2=[preco*0.5 for preco in lista_precos if preco >1000]


