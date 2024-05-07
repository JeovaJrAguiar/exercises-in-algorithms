alfabeto = "abcdefghijklmnopqrstuvxz"
vogais = "aeiou"

texto = input()

cifra = ""

def cifrar(consoanteAtual):
    distDireita = 0
    distEsquerda = 0
    vogalProxima = ""

    indiceConsoante = alfabeto.find(consoanteAtual)
    # procurando a direita
    for letra in alfabeto[indiceConsoante+1:]:
        distDireita += 1
        if letra in vogais:
            break
    
    consoanteSeguinte = ""
    alfabetoInvertido = alfabeto[::-1]
    indiceConsoanteInvertido = alfabetoInvertido.find(consoanteAtual)
    # procurando a esquerda
    for letra in alfabetoInvertido[indiceConsoanteInvertido+1:]:
        distEsquerda += 1
        if letra in vogais:
            break
    
    if distEsquerda > distDireita:
        vogalProxima = alfabeto[indiceConsoante+distDireita]
    elif distEsquerda < distDireita:
        vogalProxima = alfabetoInvertido[indiceConsoanteInvertido+distEsquerda]
    else:
        vogalProxima = alfabeto[indiceConsoante-distEsquerda]

    for letra in alfabeto[indiceConsoante+1:]:
        if letra not in vogais:
            consoanteSeguinte = letra
            break
    
    return consoanteAtual + vogalProxima + consoanteSeguinte

for letra in texto:
    if letra not in vogais:
        cifra += cifrar(letra)
    else:
        cifra += letra

print(cifra)
