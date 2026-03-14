#8. Leia um número como string e imprima o seu tipo antes e depois de converter para int.
num = input("Digite um número: ")
print(f"Tipo antes: {type(num)}")
num_int = int(num)
print(f"Tipo depois: {type(num_int)}")
