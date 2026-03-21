#[LIST - desafio] Fila: chegadas, prioridade e atendimento

#Tarefa: Inicie fila = ["Ana", "Bruno"]. Leia dois nomes e adicione (use extend). Leia um cliente prioritário e insira na posição 1. Atenda (remova e capture) o primeiro com pop(0). Exiba a fila a cada etapa.
#Use: input(), extend(), insert(), pop(), print()
#Tipos: str, list.
#Conceitos: estrutura de fila, operações de inserção/remoção, ordem.

fila = ["Ana", "Bruno"]
print(f"Fila atual: {fila}")

fila_nova = [input("Uma nova pessoa chegou a fila, qual seu nome?\n"), input("Mais uma pessoa chegou a filha, qual seu nome?\n")]
fila.extend(fila_nova)
print(f"Fila após as chegadas: {fila}")

prio = input("Digite o nome do cliente prioritário: ")
fila.insert(1, prio)

atendido = fila.pop(0)
print(f"Atendido: {atendido}")

print(f"Fila restante: {fila}")