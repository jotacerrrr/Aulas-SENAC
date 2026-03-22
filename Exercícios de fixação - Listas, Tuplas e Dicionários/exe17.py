# [TUPLE - desafio] Organizar valores sem mexer na tupla original
# Tarefa: Leia quatro números em uma tupla e exiba a tupla original, uma lista ordenada e o tipo da variável ordenada.

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
n4 = int(input("Digite o quarto número: "))

tupla_original = (n1, n2, n3, n4)

lista_ordenada = sorted(tupla_original)

print(f"Tupla original: {tupla_original}")
print(f"Lista ordenada para visualização: {lista_ordenada}")
print(f"Tipo da variável ordenada: {type(lista_ordenada)}")