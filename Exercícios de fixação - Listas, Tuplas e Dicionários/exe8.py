#[DICT] Remover uma chave com segurança

#Tarefa: Leia produto = {"nome": str, "preco": float}. Tente remover a chave "desconto" se existir, sem gerar erro. Mostre antes e depois.
#Use: input(), float(), dict.pop("chave", valor_padrao), print()
#Tipos: str, float, dict.
#Conceitos: remoção segura, estado antes/depois

nome_prod = input("Digite o nome do produto: ")
valor_prod = float(input("Digite o valor do produto: "))

produto = {
    "nome": nome_prod, 
    "preco": valor_prod
}

print(f"\nDicionário antes: {produto}")

removido = produto.pop("desconto", "Chave não encontrada")

print(f"Tentativa de remoção: {removido}")
print(f"Dicionário depois: {produto}")
