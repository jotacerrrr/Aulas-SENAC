inv = []

while True:
    item = str(input("Digite o item encontrado (digite 0 para sair): ").strip())

    if item.lower() == "sair":
        print(f"Você saiu com esses itens {inv}")
        break

    inv.append(item)
    print("item adicionado com sucesso!")
    print(inv)
    inv.sort()
    

 





    
    
