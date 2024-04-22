def quantidadeDivertido(texto):
    return texto.count(":-)")

def quantidadeChateado(texto):
    return texto.count(":-(")

def main():
    texto = input()
    qtdDivertido = quantidadeDivertido(texto)
    qtdChateado = quantidadeChateado(texto)

    emocao = qtdDivertido - qtdChateado

    if emocao == 0:
        print("neutro")
    elif emocao >= 1:
        print("divertido")
    else:
        print("chateado")

main()