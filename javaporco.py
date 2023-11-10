from random import *
from click import clear
from os import system

javaporco_mortos = 0
balas = 10

while balas>0:
    locais = ['[0] Caminonete','[1] Moita','[2] Mato','[3] Brejo', '[4] Rio', '[5] Cana', '[6] Espigão']
    locais_fugiu = ['Caminonete','Mato alto, escondido em uma moita.','Mato e correu pra longe.','brejo', 'leito do rio.', 'no passador do Canavial.', 'pasto, correndo no Espigão.']
    locais_acertou = ['Caminonete','Mato alto, escondido em uma moita.','mato, correu mas você acertou!','brejo. Você acertou', 'leito do rio. Caiu na margem.', 'no passador do Canavial. Caiu na estrada.', 'pasto, correndo no Espigão.']
    posicao = randint(1,6)
    posicao_anterior = 4
    chute = ""
    chances = 5

    while chute != posicao and chances > 0 and balas >0:      
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
            local = locais[chute]
        print()
        print(f"Javaporcos mortos: {javaporco_mortos}")
        print(f"Munição: {balas+1} \n")
        print(f"Você está em: {local}.")
        if chute == posicao_anterior:
            print("O Javaporco ESTAVA aqui!")
        else: 
            print("A Javaporco NÃO está aqui!")
        print(f"\nOpções para procurar: {locais}")
        chute = int(input("Para qual local você vai adentrar para procurar o Javaporco?"))
        posicao_anterior = posicao
        if posicao > 1 and posicao < len(locais): 
            if randint(0,1): 
                posicao +=1
            else:
                posicao -=1
        else:
            if posicao ==1:
                posicao +=1
            else:
                posicao -=1

    if(chances==0):
        
        clear()
        print("\nJAVAPORCO FUGIU!")
        print(f"Ele estava escondido no {locais_fugiu[posicao]}")
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
        
        clear()
        print("""
        _/﹋\_                      ░░░░░░░░░░░░░░░░░░░░░░
        (҂`_´) –                    ░░░░▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄
        <;︻╦╤─ ҉ – – – – – – – –   ░░░▀███████████████°▀       
                                     ░░░██▀██▀▀▀▀▀██▀▀▀
                                    ░ ░░░▀░▀░░░░░░▀ ▀ ░░░░░   
            
            """ )    
        print("Você matou um JAVAPORCO!")
        print()
        print(f"Ele estava no {locais_acertou[posicao]}")
        system("pause")
clear()
print(f"""
        #########################
        ##### VOCÊ MATOU {javaporco_mortos} ######
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
