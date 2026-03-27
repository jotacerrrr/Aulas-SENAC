"""
Desenvolver um algoritmo que automatize o cálculo de médias escolares, 
permitindo a inserção de um número ilimitado de notas e fornecendo o status final do aluno.
Contexto:
Você deve criar um programa que ajude um professor 
a lançar notas. O sistema deve ser flexível: o professor pode 
lançar 2, 5 ou 10 notas, e o programa deve calcular a média aritmética
corretamente ao final.
"""
notas = []
 
while True:
    nota = float(input("Digite a nota (digite -1 se quiser sair): "))
   
    if nota == -1:
        break
   
    notas.append(nota)
 
if len(notas) > 0:
    media = sum(notas) / len(notas)
    print("Notas:", notas)
    print(f"Média: {media:.f2}")
   
    if media >= 7:
        print("Situação: APROVADO")
    else:
        print("Situação: RECUPERAÇÃO")
else:
    print("Nenhuma nota foi digitada.")