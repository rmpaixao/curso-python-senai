import time
w = "1 0 0 1 0 1 1 1 0 1 0 1 1 0 1 1 0 0 1 0 1 1 1 0 1 0 1 1 0 1 1 1 0 0 1 0 1 1 1 0 1 0 1 1 0 1 1 0 0 1 0 1 1 1 0 1 0 1"
x = "1 0 0 1 0 1 1 1 0 1 0 1 1 0 1 1 1 0 0 1 1 0 1 1 0 0 1 0 1 1 0 0 1 0 1 1 1 0 1 0 1 1 0 1 0 1 0 1 1 1 0 1 1 1 0 1 0 1"
y = "0 1 1 0 1 1 0 0 1 0 1 1 0 1 0 1 1 0 1 1 0 0 1 0 1 1 1 0 1 0 1 1 0 1 1 0 1 0 1 1 0 1 1 1 0 0 1 0 1 1 1 1 0 0 1 0 1 1"
z = "0 1 1 1 0 1 0 1 1 0 1 1 1 0 0 1 0 1 0 0 1 0 1 1 1 0 1 0 1 1 0 1 1 0 0 1 0 1 1 1 0 1 0 0 1 0 1 1 1 0 1 0 1 1 0 1 0 1"




a = "1 0 0 1 0 1 1 1 0 1 0 1 1 0 1 1 0 0 1 0 1 1 1 0 1 0 1 1 0 1 1 1 0 0 1 0 1 1 1 0 1 0 1 1 0 1 1 0 0 1 0 1 1 1 0 1 0 1"
b = "1 0 0 1 0 1           1     1 1 1     1               0 1   0 0 1   1 1         1 1     0 1 0   1 1 0 1 1 1 0 1 0 1"
c = "0 1 1 0 1 1   0 1 0   1 0     1     1 1 0 0 1   1 1 1 0 1   1 1 0   1 0   0 1   0 1       0 1   1 1 1 1 0 0 1 0 1 1"
d = "0 1 1 1 0 1   1 1 0   1 1 0       1 0 0 1 0 1   1 0 1 0 1           0 1   1 1   0 1         1   1 0 1 0 1 1 0 1 0 1"
e = "1 0 0 1 0 1           1 1 0 1   0 0 1 0 1 1 1   1 0 1 1 0   1 1 0   1 0   1 1   1 0   1         0 1 0 1 1 1 0 1 0 1"
f = "1 0 0 1 0 1   1 0 1 0 1 1 0 1   1 0 0 1 1 0 1   0 0 1 0 1   0 0 1   1 1   0 1   1 1   1 0       1 1 0 1 1 1 0 1 0 1"
g = "0 1 1 0 1 1   0 1 0 1 1 0 1 0   1 0 1 1 0 0 1   1 1 1 0 1   1 1 0   1 0         0 1   1 0 0     1 1 1 1 0 0 1 0 1 1"
h = "0 1 1 1 0 1 0 1 1 0 1 1 1 0 0 1 0 1 0 0 1 0 1 1 1 0 1 0 1 1 0 1 1 0 0 1 0 1 1 1 0 1 0 0 1 0 1 1 1 0 1 0 1 1 0 1 0 1"




t= [w,x,y,z]
p= [a,b,c,d,e,f,g,h]

while True:
    cont = 0
    cont_ger=0




    while True and cont_ger < 50:
        cont_ger +=1
        print(t[cont])
        if cont == 3:
            cont = 0
        else:
            cont += 1
        time.sleep(0.06) 

    cont = 0

    while cont <=7:
        print(p[cont]) 
        cont +=1
        time.sleep(0.06) 


    cont = 0
    cont_ger=0

    while True and cont_ger < 50:
        cont_ger +=1
        print(t[cont])
        if cont == 3:
            cont = 0
        else:
            cont += 1
        time.sleep(0.06) 