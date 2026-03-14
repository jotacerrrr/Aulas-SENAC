#18. Leia um nome e uma nota (float), com uma casa decimal, e imprima:
nome = str(input("Qual seu nome? "))
floatnota = float(input(f"Insira sua nota {nome}: "))
print(f"Aluno {nome} ficou com nota {floatnota:.1f}")

