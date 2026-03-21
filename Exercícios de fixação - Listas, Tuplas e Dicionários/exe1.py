lista_compras = []
print(lista_compras)

while True:
    add = int(input("Quer adicionar itens a lista?\n1 - Sim\n2 - Não\n: "))

    if add == 1:
        item = input("Qual item você quer adicionar?\n: ")
        lista_compras.append(item) 
        print(f"Item '{item}' adicionado!")
        print(f"Sua lista agora: {lista_compras}")
        
    elif add == 2:
        print("Saindo...")
        break
    
    else:
        print("Opção errada")
    
print("Sua lista final")
print(lista_compras)