def main():
    aux = int(input())
    agenda = {}
    nomesSolicitados = []
    
    for i in range(1, aux+1):
        pessoa = input()
        pessoa = pessoa.split(' ')
        
        agenda[pessoa[0]] = pessoa[1]
        
    for i in range(1000):
        nomesSolicitados.append(input())
    
    for nomeSolicitado in nomesSolicitados:
        valor = agenda.get(nomeSolicitado)
        if valor is not None:
            print('{}={}'.format(nomeSolicitado, valor))
        else:
            print('Not found')
            

main()
