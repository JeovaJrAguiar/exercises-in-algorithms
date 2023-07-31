def printEspecial(s):
    impar = ""
    par = ""
    
    for index, value in enumerate(s):
        if index % 2 == 1:
            impar = impar+value
        if index % 2 == 0:
            par = par+value
    
    print(par + " " + impar)

def main():
    numberOfLines = int(input())
    
    for line in range(numberOfLines):
        s = input()
        printEspecial(s)

main()
