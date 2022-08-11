s = 0
q = 0
while True:
    num = int(input('Digite um número (E digite 0 para parar): '))
    if num == 0:
        break
    s = s + num
    q = q + 1
print('Quantidade de números digitados: ',q)
print('Soma dos valores: ' ,s)
print(f'Média aritmética:{s/q:10.2f}')
    
