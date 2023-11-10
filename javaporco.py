from random import *
from click import clear
from os import system

javaporco_mortos = 0
balas = 10

while balas>0:
    cidades = ['[0] Caminonete','[1] Moita','[2] Mata','[3] Brejo', '[4] Rio', '[5] Cana', '[6] Espigão']
    carmem = randint(1,6)
    carmem_ant = 4
    chute = ""
    chances = 5

    while chute != carmem and chances > 0 and balas >0:      
        chances-=1  
        balas-=1
        clear()
        print("""
        #########################
        ### MATA O JAVAPORCO ####
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
        print(f"Munição: {balas+1} .\n")
        print(f"Você está em: {local}.")
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
    ─▒▐▒▐▒▒▒▒▌▒─▒▒▌▒▒▐▒▒▌▒         ░░░░░░░░░░░░░░░░░░░░░░
    ──▒▀▄█▒▄▀▒───▒▀▄▒▌▄▀▒     ==   ░░░░▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄
    ─────██─────────██        ==   ░░░▀████████████████▀▀
    ░░░▄▄██▄░░░░░░░▄██▄░░░    ===  ░░░██▀██▀▀▀▀▀██▀▀▀
                                   ░░░░▀░▀░░░░░░▀ ▀ ░░░░░
            
        """)
        system("pause")
    else:
        javaporco_mortos +=1
        print("""
        _/﹋\_                      ░░░░░░░░░░░░░░░░░░░░░░
        (҂`_´) –                    ░░░░▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄
        <;︻╦╤─ ҉ – – – – – – – –   ░░░▀███████████████°▀       
                                     ░░░██▀██▀▀▀▀▀██▀▀▀
                                    ░ ░░░▀░▀░░░░░░▀ ▀ ░░░░░   
            
            """ )    
        print("Você matou um JAVAPORCO!/n")
        print(f"Ele estava escondido no {cidades[carmem]}")
        system("pause")
clear()
print(f"""
#########################
### VOCÊ MATOU {javaporco_mortos} ####
#########################
    ──▄▄█▄▄▄▄▄▄▄▄
    ██▄█▐███████████──
    ▀████████████▌▌
    ─ ▐█▐█▌ ─▐█▐█▌──
    
#########################        
##### JAVAPORCO(S) ###### 
#########################      
    """,end="")
print("")

if javaporco_mortos == 0:
    print(f"""
    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    ░█▀▀ ░█▀█ ░█ ░█▀▀ ░░█▀▀ ░█▀█░█ ░█░░░░░░
    ░█▀▀ ░█▀▀ ░█ ░█ ░░░░█▀▀ ░█▀█░█ ░█ ░░░░░
    ░▀▀▀ ░▀ ░░░▀ ░▀▀▀ ░░▀░░ ░▀░▀░▀ ░▀▀▀░░░░
    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
          """)
else:
     print(f"""           
    ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
    ░░░░░░░░░░▀█▄▀▄▀██████░▀█▄▀▄▀████▀
    ░░░░░░░░░░░░▀█▄█▄███▀░░░▀██▄█▄█▀
           """)

system("pause")
