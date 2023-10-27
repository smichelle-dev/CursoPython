nome = input("digite seu nome:")
idade = input ("digite sua idade:")
print(' 'in nome)
print(len(nome))

if nome and idade:
    print(f'seu nome é {nome}')
    print(f'seu investido é {nome[::-1]}')
if ' ' in nome:
    print('Seu nome contem espaços')
else:
    print('Seu nome não contem espaços')
    print(f'Seu nome tem{len(nome)}letras')
    print(f'a primeira letra do seu nome é {nome[0]}')
    print(f'a ultima letra do seu nome é {nome[-1]}')
    print("Desculpe, você deixou campos vazios")