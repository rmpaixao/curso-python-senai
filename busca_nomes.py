from os import system
from random import *

nomes = ['Maria', 'João', 'Antônio', 'Pedro', 'Silvio', 'Rafael', 'Gabriel', 'Rogério']
rand = randint(0,7)
nomerand = nomes[rand];
print("O nome tem "+ str(len(nomerand))+" letras")
print("Começa com a letra "+ nomerand[0])
nome = input('Digite o nome ')
if nome==nomerand:
    print("Você Acertou, o nome era ", nomerand)
else:
    print("Você Errou, o nome não era",nome,", o nome era", nomerand)
system('pause')