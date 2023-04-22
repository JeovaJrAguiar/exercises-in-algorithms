def eh_primo(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    for i in range(3, int(num**0.5)+1, 2):
        print(i)
        if num % i == 0:
            return False

    return True


def main():
    num = int(input("Insira o numero: "))
    if eh_primo(num):
        print("-> {} é primo!".format(num))
    else:
        print("-> {} não é primo!".format(num))


main()
