'''
▪ Escreva um programa que dado um inteiro n positivo calcula e
imprime a soma de todos os números
inteiros entre 1 e n.
▪ Valide a entrada do usuário, só aceite números positivos!! --> while
 ▪ Dica: use while para a validação e for para a soma.
 ▪ Por exemplo, se n = 10 então deverá ser calculado:
 ▪ 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55
 ▪ E a impressão final seria:
 ▪ A soma de 1 até 10 é: 55
'''

num = 0

#verificando se o numero é valido
while num <= 0:
    num = int(input("Digite um numero inteiro POSITIVO: "))

soma = 0 # acumulador

#so e executado SE o numero for validado
#nesse caso faz sentido separar o for do while, em outros pode estar juntos
for i in range(1, num+1):
    soma += i # soma = soma + i --> pega o valor atual de soma e add o valor de i

print(f"1 ate {num}, sua soma é: {soma}")
