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