# [TUPLE] Dias da semana com tuplas
# Tarefa: Crie uma tupla com os nomes dos sete dias da semana. Leia um número de 1 a 7 e exiba o dia correspondente.

dias = ("Domingo", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo")

indice = int(input("Digite um número de 1 a 7: "))

if 1 <= indice <= 7:
    print(f"O dia correspondente é: {dias[indice - 1]}")
else:
    print("Erro: Digite um valor entre 1 e 7.")