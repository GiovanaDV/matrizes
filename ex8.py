'''
 Faça um programa que realize a soma de duas matrizes, com mesmas dimensões. Seu programa deve
ter 2 matrizes A e B de números inteiros. A terceira matriz deve ser a soma de A com B

- matrizes precisam ter as mesmas dimensoes
'''

import numpy as np

A = np.array([
    (10, 9, 8),
    (3, 2, 4),
    (-10, 2, 5)
])


B = np.array([
    (8, 36, 9),
    (18, -20, 7),
    (12, 5, 18)
])

C = np.add(A, B) # ou C = A + B

print(C)