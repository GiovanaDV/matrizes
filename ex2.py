'''
Contagem de 0 a 100 pulando de 10 em 10.
 ▪O terminal deve ficar assim
  0
 10
 20
 30
 40
 50
 60
 70
 80
 90
 100
'''

for i in range(0, 101, 10): # 101 pq se nao ia parar no 90 --> range(n, n-1)
    print(i)