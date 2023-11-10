from random import *
from click import clear
from os import system
cidades = ['[0] Caminonete','[1] Moita','[2] Mata','[3] Brejo', '[4] Rio', '[5] Cana', '[6] Espigão']
carmem = randint(1,6)
carmem_ant = 4
chute = ""
chances = 5

while chute != carmem and chances > 0:      
    chances-=1  
    clear()
    print("""
    #########################
    ### PEGA O JAVAPORCO ####
    #########################
        ──▄▄█▄▄▄▄▄▄▄▄
        ██▄█▐███████████──
         ▀████████████▌▌
         ─ ▐█▐█▌ ─▐█▐█▌──
           
    #########################        
    # Encontre O JAVAPORCO ## 
    #########################      
        """,end="")
    print("")
    if not chute:
        local = "[0] Caminhonete"
    else:
        local = cidades[chute]
    print()
    print(f"Você está em: {local}.")
    print(f"Você tem {chances+1} balas.")
    if chute == carmem_ant:
        print("O Javaporco ESTAVA aqui!")
    else: 
        print("A Javaporco NÃO está aqui!")
    print(f"\nOpções para procurar: {cidades}")
    chute = int(input("Para qual local você vai adentrar para procurar o Javaporco?"))
    carmem_ant = carmem
    if carmem > 1 and carmem < len(cidades): 
        if randint(0,1): 
            carmem +=1
        else:
            carmem -=1
    else:
        if carmem ==1:
            carmem +=1
        else:
            carmem -=1

if(chances==0):
    print("\n\JAVAPORCO FUGIU!")
    print("""
──▒▒▒▒▒▒▒▒───▒▒▒▒▒▒▒▒
─▒▐▒▐▒▒▒▒▌▒─▒▒▌▒▒▐▒▒▌▒
──▒▀▄█▒▄▀▒───▒▀▄▒▌▄▀▒
─────██─────────██
░░░▄▄██▄░░░░░░░▄██▄░░░
             
        ░░░░░░░░░░░░░░░░░░░░░░
        ░░░░▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄
        ░░░▀████████████████▀▀
        ░░░██▀██▀▀▀▀▀██▀▀
        ░░░░▀░▀░░░░░░▀ ▀ ░░░░░
          

░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░█▀▀ ░█▀█ ░█ ░█▀▀ ░░█▀▀ ░█▀█░█ ░█░░░░░░
░█▀▀ ░█▀▀ ░█ ░█ ░░░░█▀▀ ░█▀█░█ ░█ ░░░░░
░▀▀▀ ░▀ ░░░▀ ░▀▀▀ ░░▀░░ ░▀░▀░▀ ░▀▀▀░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    """)
else:
    print("""
    ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
    ░░░░░░░░░░▀█▄▀▄▀██████░▀█▄▀▄▀████▀
    ░░░░░░░░░░░░▀█▄█▄███▀░░░▀██▄█▄█▀

    
    _/﹋\_
    (҂`_´) –
    <;︻╦╤─ ҉ – – – – – – – –           
       
          
        ░░░░░░░░░░░░░░░░▄██
        ░░░░▄████▄▄▄▄▄▄███████
        ░░▄█▀████████████▀
        ░▄▀░██▀██▀▀▀▀▀██▀▀▄
        ░░░░█▄░▀█▄░░░░▀█▄▀▀
           """ )    
    print("Você encontrou o JAVAPORCO!")
    print(f"Ele estava escondido no {cidades[carmem]}")
system("pause")