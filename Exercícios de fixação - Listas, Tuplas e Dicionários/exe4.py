#[LIST - desafio] Notas: subtituir a menor nota, ordenar e recalcular a média

#Tarefa: Leia três notas (float) em uma lista. Calcule a média. Substitua a menor nota por uma nova informada. Ordene a lista e mostre a nova média.
# Use: float(), input(), min(), list.index(), atribuição por índice, sort(), sum(), len(), print()
#Tipos: float, list.
#Conceitos: mutabilidade, ordenação in-place, média aritmética.

nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite sua terceira nota: "))

lista = [nota1,nota2, nota3]
print(f"Essas são suas notas {lista}")

media = sum(lista) / len(lista)
print(f"Sua média total é: {media:.1f}")

subst = min(lista)
indice = lista.index(subst)

nota4 = float(input(f"Recuperação da nota {subst}, Digite a nota da recuperação:  "))
lista[indice] = nota4
lista.sort()
media2 = sum(lista) / len (lista)

print(f"Lista atualizada e ordenadal: {lista}")
print(f"Nova média: {media2:.1f}")