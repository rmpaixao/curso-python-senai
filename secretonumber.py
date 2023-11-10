from random import randint
from os import system
secret_number =  randint(1,10)
num = ""
vezes = 0

print(
"""
+===================================+
| Bem vindo ao meu jogo, trouxa!    |
| Insira um número inteiro          |
| e adivinhar o número que tenho    |
| escolhidos para você.             |
| Então, qual é o número secreto?   |
+===================================+

""")

while num == secret_number:
    num = int(input("\nDigite aí otário: "))
    vezes +=1
    
print("\nAcertou Miserávi! \n\nVocê tentou ["+str(vezes)+"] vezes. \nEEEeee fela da mãe, Eu sabia que você ia acertar!\n\n")    
system('pause')
