# [TUPLE - desafio] Tupla de notas com média (sem alterar a tupla)
# Tarefa: Leia três notas (float) e armazene em uma tupla. Exiba a tupla e a média das notas.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

notas = (nota1, nota2, nota3)

media = sum(notas) / len(notas)

print(f"Tupla de notas: {notas}")
print(f"Média das notas: {media:.2f}")