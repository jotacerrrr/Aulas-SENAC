#Crie uma função que receba uma string e retorne a quantidade de caracteres que ela possui.

def contar_caracteres(texto):
    return len(texto)

frase = "Olá, mundo!"
quantidade = contar_caracteres(frase)

print(f"A string contém {quantidade} caracteres.")