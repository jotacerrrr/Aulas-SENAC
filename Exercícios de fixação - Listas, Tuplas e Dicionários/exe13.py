# [TUPLE] Contar quantas vezes um número aparece
# Tarefa: Leia quatro números inteiros e crie uma tupla. Depois leia um número e diga quantas vezes ele aparece na tupla.

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
n4 = int(input("Digite o quarto número: "))

numeros = (n1, n2, n3, n4)

pesquisa = int(input("Digite um número para contar as ocorrências: "))
contagem = numeros.count(pesquisa)

print(f"O número {pesquisa} aparece {contagem} vezes na tupla.")