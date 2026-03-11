n = input ("Nome: ")
p = (float(input("Peso: ")))
h = (float(input("Altura: ")))

imc = p / (h **2)
print (f"IMC de {n}: {imc:.2f}")
baixo_p = imc < 18.5
normal = (imc >= 18.5) and (imc < 25)
sobrepeso = (imc >= 25) and (imc <30)
obesidade = imc >= 30

print ("Baixo peso?", baixo_p)
print ("Normal?", normal)
print ("Sobrepeso?", sobrepeso)
print ("Obesidade", obesidade)

