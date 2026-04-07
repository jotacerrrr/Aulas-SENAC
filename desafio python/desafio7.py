#Crie uma função que receba uma palavra e verifique se ela é um palíndromo
#(lê igual de trás para frente).

def verificar_palindromo(palavra):
    
    palavra_formatada = palavra.replace(" ", "").lower()
    
    return palavra_formatada == palavra_formatada[::-1]

print(verificar_palindromo("Arara")) 
print(verificar_palindromo("Python"))