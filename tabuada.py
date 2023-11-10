from os import system
tabuada = 1
print()

input("Vamos utilizar o WHILE para gerar as tabuadas! Pressione [ENTER]..")

while tabuada <= 10:
    count = 0
    while count <= 10:
        print(tabuada,"x",count,"=",tabuada*count)
        count += 1
    tabuada += 1
    print()

input("Fizemos tudo com WHILE. Agora vamos utilizar o FOR. Pressione [ENTER]..")

tabuada = 1
for tabuada in range(1,11):
    count = 0
    for count in range(0,11):
        print(tabuada,"x",count,"=>",tabuada*count)
    print()
input("Acabou!! pressione [ENTER] para sair...")



