#▪ Após o comando if, a linha de comando termina com dois pontos (:) isso indica o anuncio de um
#bloco de linha a seguir (no qual vai informar qual é o script de execução). O bloco continua até a
#primeira linha com deslocamento diferente.

#PROGRAMA - LE DOIS VALORES E IMPRIME QUAL É O MAIOR
a = int(input("Entre com o primeiro valor: "))
b = int(input("Entre com o segundo valor: "))
if a > b:
    print ("O primeiro valor é maior")
if b > a:
    print ("O segundo valor é maior")
if a == b:
    print ("Os números são iguais")
