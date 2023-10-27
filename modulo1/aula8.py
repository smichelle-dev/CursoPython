nome ='Beatriz'
altura = 1.6499
peso =70

resultado = f'{nome} é gata e tem {altura} com um peso de:{peso}'
resultado = f'{nome} é gata e tem {altura:.2f} com um peso de:{peso}' #formatação das casas decimais


print(resultado)

a="lucas"
b="pedro"
c=1.1
formatacao ='a={} b={} c={:.2f}'.format(a,b,c)
print(formatacao)