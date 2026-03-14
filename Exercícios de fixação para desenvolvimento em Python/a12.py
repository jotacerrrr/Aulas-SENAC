#12. Leia 3 notas (float) e imprima a média com duas casas decimais.
nota1 = float(input("Qual sua primeira nota?: "))
nota2 = float(input("Segunda nota: "))
nota3 = float(input("Terceira nota: "))
media_notas = (nota1+nota2+nota3)/3
print(f"Sua média é: {media_notas:.2f}.")

