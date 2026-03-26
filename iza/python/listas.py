nome = 'Izabele'
print( f'Meu nome e: {nome}')

nome = 'maria' 
print(f'meu nome e:{nome}')

nomes = [ 'izabele', 'maria']

print(nomes[0])
print(nome[1])

apostulos = ['Matheus' , 'Tiago', 'Lucas', 'judas', 'pedro']

# percorr4endo a lista posiçoa por posiçao 
for apostolos in apostolos:
    print(apostolos)

    #adicionando item no final da list a
    print(apostulos)
    apostolos.append('joao')
    print(apostolos)

    #adicionando item na posiçao desejada. exemplo posiçao 2 
    apostulos.insert(2,'simao')
    print(apostolos)

    #expandidndo a lista com novos elementos 
    cavaleiros= ['seiya', 'shiryu']
    print(cavaleiros)

    cavaleiros.extend(['IKKi', 'yoga', 'shun'])
    print(cavaleiros)

    
    # excluindo itens de uma lista 
    cavaleiros.pop()
    print(cavaleiros)

    cavaleiros.pop(0)
    print(cavaleiros)

    #excluindo por valor

    print(apostolos)
    apostolos.remove('judas')
    print(apostolos)
    

    alunos = ['Victor', 'lucas', 'gabriel', 'lucas', 'amanda', ' daniel']
    print(alunos)
   # alunos.remove('lucas')
   #print(alunos)

    for indice ,aluno in enumerate(alunos):
      if aluno == 'lucas':
        alunos.pop(indice)

        print(alunos)
        

        numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        impares = []
        pares = []


 
    for  numero in numeros:
            if numero % 2 !=  0:
                impares.append(numero)
            elif numero % 2 == 0:
                pares.append(numero)

    print(impares)
    print(pares) 

    print( apostolos)
    apostolos.sort()
    print(apostolos)
    apostolos.reverse()
    print(apostolos)

    print(cavaleiros)
    cavaleiros.clear()
    print(cavaleiros)

    print(pares)
    del pares 
    print(pares)
    


