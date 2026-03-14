#14. Leia uma quantidade de minutos (int) e converta para horas e minutos (ex.: 130 -> 2h10)
minutos = int(input("Insira uma certa quantidade de minutos: "))
horas_total = minutos//60
resto = minutos%60
print(f"{horas_total}h{resto}")

