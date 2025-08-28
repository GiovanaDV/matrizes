'''
Escreva um algoritmo que lê um número inteiro n > 0 e preenche um vetor de caracteres de n
posições.
▪ Depois de preencher o vetor, você deverá inverter o seu conteúdo, ou seja, trocar o conteúdo da
primeira posição (0) com a ´ultima (n − 1) a segunda com a penúltima e assim por diante até que o
vetor esteja invertido.
'''

import numpy as np

num = 0

while num <= 0:
    num = int(input("Digite um numero inteiro positivo: "))

vetor = np.random.uniform(0.0, num, num)
print(f"vetor: {np.round(vetor, 2)}")
print(f"vetor invertido:{np.flip(np.round(vetor, 2))}") # metodo que inverte os indices do vetor
