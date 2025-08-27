'''
Escreva um algoritmo que recebe um inteiro positivo n e imprime todos os
divisores positivos de n.
 ▪ Utilize o laço for.
 ▪ Exemplo:
Suponha que n = 28, nessa situação devemos imprimir os números
1, 2, 4, 7, 14 e 28, que são todos os divisores do 28.
 ▪ Dica: para o número ser divisor de n, a divisão precisa ter resto nulo
'''

n = 0

while n <= 0:
    n = int(input("Digite um numero inteiro positivo: "))

for i in range(1, n+1):
    if n % i == 0:
        print(i)

# ERRO que fiz: i % n == 0 --> print era so o 28, PQ?
# estava fazendo i dividido por 28, o unico divisor que ele tera sera quando i = n, pq em todas as outras situacoes i é menor que n
# assim, quando inverti deu certo
