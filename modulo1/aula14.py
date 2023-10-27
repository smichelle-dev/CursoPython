"""
interporlação de string
s - string
d e  i - int
f - float
x e X - hexadecimal 
"""


nome ='luiz'
preco =1000.95897643
variavel = '%s, o preco total foi R$%.2f' % (nome, preco)
variavel = 'Luiz, o preco total foi R$1000.95 '
print (variavel)

"""
formatação de string
"""

variavel = 'ABC'
print (f'{variavel}')
print (f'{variavel: >10}') #preenche o lado esquerdo com espaços
print (f'{variavel: <10}') #preenche o lado direito  com espaços
print (f'{variavel: ^10}') #preenche o centro  com espaços
print (f'{1000.2982216493241215:.2f}') #


