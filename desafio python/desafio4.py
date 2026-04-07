#Crie uma função que receba uma lista de números e retorne o maior número da lista. 

def encontrar_maior(lista):
    if not lista:  
        return None
    return max(lista)

numeros = [10, 5, 23, 8, 42, 1]
resultado = encontrar_maior(numeros)
print(f"O maior número é: {resultado}")

