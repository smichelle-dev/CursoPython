def multiplicar (*args):
    total = 1
    for numero in args:
        total*= numero
        return total
    
    multiplicacao = multiplicar(25,96,35,822,26)
    print(multiplicacao)