from random import *
from click import clear
from os import system
cidades = ['[0] Base Secreta','[1] Miami','[2] Cidade do México','[3] São Paulo', '[4] Rio de Janeiro', '[5] Santiago', '[6] Buenos Aires']
carmem = randint(1,6)
carmem_ant = 4
chute = ""
chances = 5

while chute != carmem and chances > 0:      
    chances-=1  
    clear()
    print("""
    #########################
    # ESPIÃ CARMEM SANDIEGO #
    #########################
    _/﹋\_
    (҂`_´) –
    <;︻╦╤─ ҉ – – – – – – – – 
    #########################        
    ### Encontre a Espiã #### 
    #########################      
        """,end="")
    print("")
    if not chute:
        local = "Base Secreta"
    else:
        local = cidades[chute]
    print()
    print(f"Você está em: {local}.")
    print(f"Você tem {chances+1} passagens.")
    if chute == carmem_ant:
        print("A Carmem Sandiego ESTAVA aqui!")
    else: 
        print("A Carmem Sandiego NÃO está aqui!")
    print(f"\nOpções de voo: {cidades}")
    chute = int(input("Para qual cidade você deseja viajar para procurá-la?"))
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
    print("\n\nCarmem Sandiego FUGIU!")
    print("""
        ▬▬▬.◙.▬▬▬
        ═▂▄▄▓▄▄▂
        ◢◤ █▀▀▀████▄▄▄▄▄▄◢◤
        █▄ █ O/ ██▀▀▀▀▀▀▀╬
        ◥█████◤
        ══╩══╩══
    
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
        
        """ )    
    print("Você encontrou a Carmem Sandiego!")
    print(f"Ela estava em {cidades[carmem]}")
system("pause")