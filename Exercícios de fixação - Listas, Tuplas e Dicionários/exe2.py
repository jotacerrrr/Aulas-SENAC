#[LIST] Remova um número se ele existir

#Tarefa: Leia quatro inteiros e crie uma lista. Leia um valor alvo e remova se ele estiver na lista. Mostre o tamanho antes e depois.
# Use: int(), input(), in, remove(), len(), print()
# Tipos: int, list.
# Conceitos: teste de pertencimento, tratamento simples de remoção, função len().

n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
n3 = int(input("Digite um número: "))
n4 = int(input("Digite um número: "))

list = [n1,n2,n3,n4]

remove = int(input("Digite o valor que deseja remover: "))

tamanho = len(list)
print(tamanho)

if remove in list:
    list.remove(remove)
    print(f"O valor {remove} foi removido.")
else:
    print(f"Valor não encontrado na lista.\nEsse são os valores na sua lista. {list}")
    
tamanho = len(list)
print(f"Tamanho depois: {tamanho}")
print(f"Lista final: {list}")