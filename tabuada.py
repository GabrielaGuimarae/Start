tab = int(input('Digite o número da tabuada: '))
inicio = int(input('Digite o número de ínicio da tabudada: '))
fim = int(input('Digite o número do fim da tabuada: '))

for c in range (fim - inicio + 1):
    print(f'{tab} X {inicio} = {tab*inicio}')
    inicio +=1
    
