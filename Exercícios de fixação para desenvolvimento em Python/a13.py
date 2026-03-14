#13. Leia o salário (float) e um percentual de aumento (float) e calcule o novo salário.
sal = float(input("Qual seu salário: "))
aument = float(input("Vai receber um aumento de quantos %? "))
new_sal = sal*(aument/100)
salario_final = sal+new_sal
print(f"Você irá receber {salario_final}")

