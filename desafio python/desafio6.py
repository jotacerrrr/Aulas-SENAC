#Crie uma função que receba uma lista de números e retorne a média dos valores.

def calcular_media(lista):
    if not lista: 
        return 0
    
    return sum(lista) / len(lista)

numeros = [10, 20, 30, 40, 50]
media = calcular_media(numeros)
print(f"A média dos valores é: {media}")