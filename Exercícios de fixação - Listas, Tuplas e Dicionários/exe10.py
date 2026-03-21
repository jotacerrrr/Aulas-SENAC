#[DICT  - desafio] Agenda (CRUD simples) com ordenação de nomes

#Tarefa: agenda = {"Ana", "1111-1111", "Bruno": "2222-2222"}
#Adicionar um novo contato (nome→telefone)
#Atualizar o telefone de um contato informado (se existir)
#Remover um contato pelo nome (se existir)
#Exibir a lista ordenada de nomes de contatos
#Tipos: str, dict, list (para a lista ordenada, se desejar armazenar).Conceitos: CRUD em dicionários, teste de existência, ordenação de chaves.Use: input(), acesso/atribuição agenda[nome] = tel, in, pop(), sorted(agenda.keys()), print()

agenda = {"Ana": "1111-1111", "Bruno": "2222-2222"}

novo_nome = input("Digite o nome do novo contato: ")
novo_tel = input("Digite o telefone: ")
agenda[novo_nome] = novo_tel

nome_att = input("Digite o nome para atualizar o telefone: ")
if nome_att in agenda:
    novo_tel_att = input("Digite o novo telefone: ")
    agenda[nome_att] = novo_tel_att

nome_rem = input("Digite o nome para remover: ")
if nome_rem in agenda:
    agenda.pop(nome_rem)

nomes_ordenados = sorted(agenda.keys())

print("\nAgenda Ordenada:")
for nome in nomes_ordenados:
    print(f"{nome}: {agenda[nome]}")