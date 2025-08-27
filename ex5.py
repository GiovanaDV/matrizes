'''
▪ Determine e mostre todos os números primos no intervalo de 2 a 2000.
 Dicas:
▪ Para resolver esse problema, primeiro faça um algoritmo que
verifica se um número inteiro qualquer é
primo ou não.
 ▪ A seguir, com esse código em mãos, faça os ajustes
 necessários para mostrar todos os números primos
no intervalo solicitado.
 ▪ Você precisará colocar uma estrutura de repetição dentro da outra.
 ▪ Laços aninhados!!!!
'''

# num é primo quando é maior que 1 e tem apenas 2 divisores -> 1 e ele mesmo
# se divisores > 2 ele nao e primo

for i in range(2, 2001):
    primo = True # reinicializa ele para cada numero i, se colocar fora do loop primo fica False mesmo que se os proximos nums forem primos
    for j in range(2, i):
            if i % j == 0: # o numero i é divisivel por j?
                primo = False
    if primo: # mesma coisa que if primo == True --> pq so vai rodar o if se for true
        print(i)

