'''
 Faça um programa que exiba a mensagem “Olá, Mundo”.
 ▪ Essa mensagem deverá ser exibida repetidamente.
 ▪ Ao final de toda iteração da repetição, você deve perguntar ao usuário
 se ele deseja exibir a mensagem
novamente.
 ▪ Se sim, exiba novamente. Senão, saia do loop e exiba a mensagem “Fim”
'''

resposta = "sim"

while resposta == "sim":
    print("Hello World!")
    resposta = input("Deseja ver a mensagem novamente?")

else:
    print("fim")

