#[DICT] Criar e exibir dicionário de aluno

#Tarefa: Leia nome e idade. Crie aluno = {"nome": ..., "idade": ...} e exiba o dicionário e seu tipo.
# Use: input(), int(), literal {}, acesso por chave dict["chave"], print(), type()
#Tipos: str, int, dict.
#Conceitos: mapeamento chave-valor, criação e exibição.

nome_usuario = input("Digite seu nome: ")
idade_usuario = int(input("Digite sua idade: "))

aluno = {
    "nome": nome_usuario,
    "idade": idade_usuario
}
print(f"Dicionário criado: {aluno}")

print(f"O nome registrado é: {aluno['nome']}")

print(f"O tipo da variável é: {type(aluno)}")

#7 [DICT - CONTINUIDADE DO EXERCÍCIO ANTERIOR] 
#Adicionar uma nova chave nota
#Tarefa: Partindo de um aluno com nome e idade, leia uma nota (float) e adicione a chave "nota". Exiba o dicionário.
#Use: float(), input(), atribuição dict["nota"] = valor, print()
#tipos: float, dict.
#Conceitos: atualização/adição de chave, tipos numéricos.

nota_usuario = float(input("Digite sua nota: "))
aluno ["nota"] = nota_usuario

print(f"{aluno}")

print(f"A nota de {aluno['nome']} é {aluno['nota']:.1f}")

