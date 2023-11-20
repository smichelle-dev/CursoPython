def duplicar (numero):
    return numero*2

def triplicar (numero):
    return numero*3

def quadruplicar (numero):
    return numero*4

print(duplicar(2))

print(duplicar(8))

print(duplicar(78))

################


def criar_multiplicador(multiplicador):
     def multiplicar (numero):
         return numero*multiplicador
     return multiplicar

dupli =criar_multiplicador(2)
tripli =criar_multiplicador(3)
quadru =criar_multiplicador(4)

