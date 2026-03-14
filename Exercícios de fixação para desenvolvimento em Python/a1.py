# 1. Peça ao usuário seu nome e cumprimente utilizando a função print(), ex.: "Olá, Carol!"

nome = str(input("Qual seu nome? "))
print(f"Olá {nome}, tudo bem com você? ")

# 2. Peça ao usuário sua idade e exiba na tela: "Você tem {idade} anos!"

idade = int(input("Quantos anos você tem? "))
print(f"Você tem {idade} anos de idade")

#3. Leia o nome e a cidade da pessoa e imprima: "{nome} mora em {cidade}."

cidade = str(input(f"E onde você mora {nome}? "))
print(f"Você mora em {cidade}.")

#4. Leia um número e imprima o dobro dele.

dobro = int(input("Insira um número, e eu vou entregar o dobro: "))
dobro2 = dobro*2
print(f"Aqui está  o dobro do número que você falou {dobro2}")

#5. Leia dois números inteiros e imprima a soma.
n1 = int(input("Insira um número para somar: "))
n2 = int(input("Insira outro número: "))
n3 = n1+n2
print(f"aqui está a soma desses números {n3}")

#6. Leia a altura (em metros) como float e imprima: "Sua altura é {altura}m"
h = float(input("Qual a sua altura? "))
print(f"Você tem: {h} metros")

#7. Leia dois números decimais (float) e imprima a média. 

d1 = float(input("Insira um número decimal: "))
d2 = float(input("Insira outro número decimal: "))
d3 = (d1+d2)/2
print(f"A média desse número é {d3:.2f}")

#8. Leia um número como string e imprima o seu tipo antes e depois de converter para int.
num = input("Digite um número: ")
print(f"Tipo antes: {type(num)}")
num_int = int(num)
print(f"Tipo depois: {type(num_int)}")

#9. Leia o preço de um produto e imprima o preço com 10% de desconto.
prod = float(input("Qual valor do produto? R$ "))
desc = prod * 0.90
print(f"O valor R com 10% de desconto vai ficar R${desc}.")

#10. Leia o raio de um círculo (float) e calcule a área, utilize π = 3.14.

cir = float(input("Insira o raio de um círculo. "))
pi = 3.14
raio_cir = 3.14 * (cir**2)
print(f"A área desse círculo é {raio_cir}")

#11. Leia a distância (km) e o tempo (h), calcule a velocidade média.
km = float(input("Quantos km você andou: "))
tempo = float(input("Por quanto tempo (h): "))
mat = (km+tempo) / 2
print(f"A velocidade média foi {mat}")

#12. Leia 3 notas (float) e imprima a média com duas casas decimais.
nota1 = float(input("Qual sua primeira nota?: "))
nota2 = float(input("Segunda nota: "))
nota3 = float(input("Terceira nota: "))
media_notas = (nota1+nota2+nota3)/3
print(f"Sua média é: {media_notas}.")

#13. Leia o salário (float) e um percentual de aumento (float) e calcule o novo salário.
sal = float(input("Qual seu salário: "))
aument = float(input("Vai receber um aumento de quantos %? "))
new_sal = sal*(aument/100)
newnew_sal = sal+new_sal
print(f"Você irá receber {newnew_sal}")

#14. Leia uma quantidade de minutos (int) e converta para horas e minutos (ex.: 130 -> 2h10)
minutos = int(input("Insira uma certa quantidade de minutos: "))
horas_total = minutos//60
resto = minutos%60
print(f"{horas_total}h{resto}")

#15. Leia o nome e a idade e imprima exatamente neste formato: 
print(f"Nome: {nome} | Idade: {idade} anos")

#16. Leia dois int (a e b) e imprima: 
int1 = int(input("Insira um número: "))
int2 = int(input("Insira um número novamento: "))

plus = int1+int2
less = int1-int2
t_each_other = int1*int2
print(f"{int1} + {int2} = {plus} | {int1} - {int2} = {less} | {int1} x {int2} = {t_each_other}")

#17. Leia um float e imprima com 2 casas decimais
floatnum = float(input("Insira um número decimal com + de 5 casas após a vírgula: "))
print(f"{floatnum:.2f}")

#18. Leia um nome e uma nota (float), com uma casa decimal, e imprima:
floatnota = float(input(f"Insira sua nota {nome}: "))
print(f"Aluno {nome} ficou com nota {floatnota} ")

#19. Leia o ano de nascimento (int) e imprima a idade estimada. (considere ano atual = 2026).
ano = int(input("Em que ano você nasceu? "))
estimativa_age = 2026-ano
print(f"Sua idade estimada é {estimativa_age}")
