#[LIST] Atualizar elemento com uma operação

#Tarefa: Crie uma lista com três inteiros. Atualize o último elemento para a soma dos dois primeiros. Exiba a lista.
# Use: int(), input(), indexação lista[i], print()
# Tipos: int, list.
# Conceitos: operadores aritméticos (+), acesso/atribuição por índice.

n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
n3 = int(input("Digite um número: "))

list = [n1,n2,n3]
print(f"Lista: {list}")

sum = list [0] + list [1]

list [2] = sum

print(f"Lista atualizada: {list}")
