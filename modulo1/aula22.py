#texto = 'Python'
#i=0
#tamanho_string = len (texto)
#while i < tamanho_string:
#  print(texto[i], i)
#   i+=1

texto = 'Python'

novo_texto = ''
for letra in texto:
    novo_texto +=f'*{letra}'
    print(letra)
print(novo_texto)

numeros = range(10)
numeros = range(5, 10)
numeros = range(5, 100, 2)
print(numeros)


numeros = range(0,500,2) #todos os numeros pares de 0 a 500

for numero in numeros:
    print(numero)

