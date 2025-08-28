'''
 Escreva um algoritmo que recebe um número inteiro n > 0, cria um vetor de números reais com n
posições e preenche o vetor com n números aleatórios reais.
▪ Depois de preenchido o vetor, imprima na tela todos os números gerados.
'''

import numpy as np

num = 0

while num <= 0:
    num = int(input("Digite um numero inteiro positivo: "))

vetor = np.random.uniform(0.0, num, num)
print(np.round(vetor, 2)) # como decidir quantas casas mostrar em um vetor!!!
