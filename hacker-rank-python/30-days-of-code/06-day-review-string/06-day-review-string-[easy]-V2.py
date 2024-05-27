numberInputs = int(input())

for n in range(numberInputs):
    word = input()
    even = ""
    odd = ""
    for i, value in enumerate(word):
        if i%2 == 0:
            even += value
        else:
            odd += value
            
    print(even + " " + odd)
