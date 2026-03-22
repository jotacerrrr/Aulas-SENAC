# [DICT - desafio] Agenda (CRUD simples) com ordenação de nomes
# Tarefa: agenda = {"Ana": "1111-1111", "Bruno": "2222-2222"}
# Adicionar um novo contato (nome→telefone)
# Atualizar o telefone de um contato informado (se existir)
# Remover um contato pelo nome (se existir)
# Exibir a lista ordenada de nomes de contatos

agenda = {"Ana": "1111-1111", "Bruno": "2222-2222"}
print(f"Essa é a sua lista atual de contatos: {agenda}")

nome_novo = input("Digite o nome do novo contato: ")
tel_novo = input("Digite o telefone (utilize esse formato 0000-0000): ")
agenda[nome_novo] = tel_novo
print(f"Agenda atualizada: {agenda}")

nome_att = input("Digite o nome para atualizar o telefone: ")
if nome_att in agenda:
    novo_tel_att = input("Digite o novo telefone: ")
    agenda[nome_att] = novo_tel_att
print(f"Agenda: {agenda}")

nome_rem = input("Digite o nome para remover: ")
agenda.pop(nome_rem, None)

nomes_ordenados = sorted(agenda.keys())

for nome in nomes_ordenados:
    print(f"{nome}: {agenda[nome]}")