#Crie uma função que receba um número e informe se ele é PAR ou ÍMPAR. 

def imp_par(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return"impar"

num = 10
num2 = 11
print(f"O número {num} é {imp_par(num)}. ")
print(f"O número {num2} é {imp_par(num2)}. ")