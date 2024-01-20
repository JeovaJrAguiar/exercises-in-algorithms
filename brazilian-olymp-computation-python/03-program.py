def quadrante(x, y):
    if y>0 and x>0:
        print("Primeiro quadrante")
    elif y>0 and x<0:
        print("Segundo quadrante")
    elif y<0 and x>0:
        print("Terceiro quadrante")
    elif y<0 and x<0:
        print("Quarto quadrante")
    elif y!=0 and x==0:
        print("Eixo Y")
    elif y==0 and x!=0:
        print("Eixo X")
    elif y==0 and x==0:
        print("Origem")


def main():
    print("Um ponto no plano carteiano.")
    x = int(input("x: "))
    y = int(input("y: "))

    quadrante(x,y)
