#[DICT - desafio] Atualizar preço e quantidade; calcular o total 

#Tarefa: Leia produto = {"nome": str, "preco": float, "quantidade": int}. Aplique aumento percentual ao preço e some 2 unidades na quantidade. Calcule total = preco * quantidade e exiba.
#Use: float(), int(), input(), acesso/atribuição por chave, print()
#Tipos: str, float, int, dict.
#Conceitos: operadores aritméticos (*, +), atualização de valores no dict.

nome = input("Digite o nome do produto: ")
preco = float(input("Digite o preço unitário: "))
quantidade = int(input("Digite a quantidade em estoque: "))

produto = {
    "nome": nome,
    "preco": preco,
    "quantidade": quantidade
}

print(f"\n--- Estado Inicial ---")
print(produto)

taxa_aumento = 1.10  

produto["preco"] = round(produto["preco"] * taxa_aumento, 2)
produto["quantidade"] += 2


total_estoque = produto["preco"] * produto["quantidade"]

print(f"\n--- Produto Atualizado ---")
print(f"Nome: {produto['nome']}")
print(f"Novo Preço: R$ {produto['preco']:.2f}")
print(f"Nova Quantidade: {produto['quantidade']}")
print(f"Valor Total em Estoque: R$ {total_estoque:.2f}")

print(f"\nDicionário final limpo: {produto}")