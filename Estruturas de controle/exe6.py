#6. Faça uma calculadora simples contendo as 
# operações: soma, subtração, divisão e multiplicação. 
# Solicite ao usuário que informe dois número e que informe também a 
# operação que deseja realizar (+, -, /, *) e depois exiba o resultado.

num1 = float(input("Informe o primeiro número: "))
num2 = float(input("Informe o segundo número: "))
operacao = input("Informe a operação (+, -, /, *): ")
 
if operacao == '+':
    resultado = num1 + num2
    print(f"Resultado: {resultado}")
elif operacao == '-':
    resultado = num1 - num2
    print(f"Resultado: {resultado}")
elif operacao == '*':
    resultado = num1 * num2
    print(f"Resultado: {resultado}")
elif operacao == '/':
    # Verificação para evitar divisão por zero
    if num2 != 0:
        resultado = num1 / num2
        print(f"Resultado: {resultado}")
    else:
        print("Erro: Não é possível dividir por zero.")
else:
    print("Operação inválida.")