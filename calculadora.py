from click import clear
def conta(n1, n2, s):
    n1 = int(n1)
    n2 = int(n2)
    if s == "+":
        return n1+n2
    elif s == "-":  
        return n1-n2  
    elif s == "/":  
        return n1/n2  
    elif s == "*":
        return n1*n2

mem = 0
while True:
    clear()
      
    print("""
####### CALCULADORA #######
       """,end="")
    print("""
===========================
|        |        |        |  
|    1   |    2   |    3   |  
|        |        |        |  
----------------------------
|        |        |        |  
|    4   |    5   |    6   |  
|        |        |        |  
----------------------------  
|        |        |        |  
|    7   |    8   |    9   |  
|        |        |        |  
===========================
""") 
    print("""
===========================
|          
| = """+str(float(mem))+""" 
|              
===========================
""")
    exp = input("=")


    if format('+' in exp)=="True":
        sin = "+"
        exp = exp.split("+")   
    elif format('-' in exp)=="True":  
        sin = "-"
        exp = exp.split("-")   
    elif format('/' in exp)=="True":
        sin = "/"
        exp = exp.split("/")   
    elif format('*' in exp)=="True":
        sin = "*"
        exp = exp.split("*")
    else:
        mem = exp
        continue

    if exp[0] and exp[1]:
        mem = conta(exp[0],exp[1],sin)
    elif (mem or mem==0) and exp[1]:
        mem = conta(mem, exp[1],sin)
    else:
        continue
    print(mem)