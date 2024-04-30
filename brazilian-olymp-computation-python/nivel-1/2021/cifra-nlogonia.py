alfabeto = "abcdefghijklmnopqrstuvwxz"
vogai = "aeiou"
consoante = "bcdfghijklmnpqrstvxz"

texto = input()
cifra = "" 

def add():
    

for letra in texto:
    letra = letra.lower
    if not(letra in consoante):
        cifra.append(letra)
        
    else:
        cifra.append(letra)

print(cifra)

