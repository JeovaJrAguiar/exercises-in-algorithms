alfabeto = "abcdefghijklmnopqrstuvxz"
vogais = "aeiou"

texto = input()

cifra = ""

# cifra uma consoante em uma tríade
def cifrar(consoanteAtual):
    distDireita = 0
    distEsquerda = 0
    vogalProxima = ""

    # procurando vogal à direita
    indiceConsoante = alfabeto.find(consoanteAtual)
    for letra in alfabeto[indiceConsoante+1:]:
        distDireita += 1
        if letra in vogais:
            break
    
    # procurando vagal à esquerda
    consoanteSeguinte = ""
    alfabetoInvertido = alfabeto[::-1]
    indiceConsoanteInvertido = alfabetoInvertido.find(consoanteAtual)
    for letra in alfabetoInvertido[indiceConsoanteInvertido+1:]:
        distEsquerda += 1
        if letra in vogais:
            break
    
    # definindo qual a vogal mais proxima
    if distEsquerda > distDireita:
        vogalProxima = alfabeto[indiceConsoante+distDireita]
    elif distEsquerda < distDireita:
        vogalProxima = alfabetoInvertido[indiceConsoanteInvertido+distEsquerda]
    else:
        vogalProxima = alfabeto[indiceConsoante-distEsquerda]

    # define a consoonte seguinte
    for letra in alfabeto[indiceConsoante+1:]:
        if letra not in vogais:
            consoanteSeguinte = letra
            break
    
    # retorna a concatenação dos 3 elementos
    return consoanteAtual + vogalProxima + consoanteSeguinte

# percorre a entrada em busca de consoantes para poder cifrar as consoantes
for letra in texto:
    if letra not in vogais:
        cifra += cifrar(letra)
    else:
        cifra += letra

print(cifra)
