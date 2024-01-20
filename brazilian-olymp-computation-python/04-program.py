def lanche(codigo, quantidade):
    total = 0.0
    if codigo == 1:
        total = quantidade * 4.00
    elif codigo == 2:
        total = quantidade * 4.50
    elif codigo == 3:
        total = quantidade * 5.00
    elif codigo == 4:
        total = quantidade * 2.00
    else:
        total = quantidade * 1.50

    print(f'{total:.2f}')

def main():
    codigo = int(input('Codigo: '))
    quantidade = int(input('Quantidade: '))

    lanche(codigo, quantidade)

main()
