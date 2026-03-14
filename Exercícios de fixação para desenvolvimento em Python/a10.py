#10. Leia o raio de um círculo (float) e calcule a área, utilize π = 3.14.

cir = float(input("Insira o raio de um círculo. "))
pi = 3.14
raio_cir = pi * (cir**2)
print(f"A área desse círculo é {raio_cir:.2f}")
