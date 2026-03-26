def soma(numero1, numero2):
    """ 
     esta funçao recebe dois numeros inteiros e realiza a 
     soma dos mesmo.
     """
    soma = numero1 + numero2
    print(f'o resultado da sua soma e {soma}')


def sub(numero1, numero2):
    """ 
     esta funçao recebe dois numeros inteiros e realiza a 
     sub dos mesmo.
     """
    sub = numero1 - numero2
    print(f'o resultado da sua sub e {sub}')


def menu():
    print('1 - somar')
    print('2 - subtrair')
    opcao = input(' o que deseja realizar?')
    return opcao
    


