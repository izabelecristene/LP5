import os 
from funcoes_exemplos import soma, sub, menu 

continuar = 's'
while continuar != 'n':
  os.system('cls')
  opcao = menu()


  numero1 = int(input("informe o primeiro numero:"))
  numero2 = int(input("informe o segundo numero:"))

  if opcao == '1':
    soma (numero1, numero2)

  elif opcao == 2:
    sub(numero1,numero2)
  else:     
     print('opcao invalida')

continuar = input ('deseja realizar outra soma s/n')




