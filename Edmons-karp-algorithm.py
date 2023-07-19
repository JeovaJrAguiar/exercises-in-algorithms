# Universidade Federal do Ceará - campus Crateús
# Ciência da computação - Algoritmos em Grafos 2023.1
# Aguiar - 495586 

# Esse algoritmo opera sobre uma rede de fluxo e trabalha conhecimentos sobre fluxo maximo/corte minimo 
# Seu objetivo é encontrar o fluxo máximo de uma rede de fluxo, atravéz do algoritmo Edmons-karp, que é uma adaptação do algortimo de ford-fullkerson

# cada vertice eh: ['seu identificador', True or false (visitado ou não), array de are encontrar]
vertices = [['s', False, []], ['v1', False, []], ['v2', False, []], ['v3', False, []], ['v4', False, []], ['t', False, []]]

# cada aresta eh: ['vertice saida', 'vertice chegada', fluxo, capacidade)]
arestas = [
    ['s', 'v1', 11, 16],
    ['s', 'v2', 8, 13],
    ['v1', 'v3', 12, 12],
    ['v2', 'v1', 1, 4],
    ['v2', 'v4', 11, 14],
    ['v3', 'v2', 4, 9],
    ['v3', 't', 15, 20],
    ['v4', 'v3', 7, 7],
    ['v4', 't', 4, 4]
]
# retorna um array de arestas, aquelas arestas
def find_successors(grafo, vertice):
    sucessores = list(filter(lambda aresta: aresta[0] == vertice[0], grafo[1]))
    return sucessores

# retorna se o vertice foi visitado ou não
def is_visited(grafo, verticeAtual):
    for vertice in grafo[0]:
        if vertice[1] and vertice[0] == verticeAtual[0]:
            return True
    return False 

# busca um vertice no grafo baseado 
def find_vertex(grafo, vertice_identificador):
    for vertice in grafo[0]:
        #print(f"{vertice} : {vertice_identificador}")
        if vertice[0] == vertice_identificador:
            print(vertice)
            return vertice
    print("------")

# realiza a busca em profundidade
def DFS(grafo, fonte, sumidouro, caminho):
    indexAtual = grafo[0].index(find_vertex(grafo, fonte))

    grafo[0][indexAtual][1] = True

    if fonte == sumidouro:
        return True
    
    sucessores = find_successors(grafo, fonte)

    for aresta in sucessores:
        vertice = find_vertex(grafo, aresta[1])

        if not is_visited(grafo, vertice):
            caminho.append(aresta)

            if DFS(grafo, vertice, sumidouro, caminho):
                return True

            # remove a aresta do caminho se não leva ao destino
            caminho.pop()

# retorna um caminho aumentante (conjunto de arestas)
def find_augmenting_path(grafo, fonte, sumidouro):
    caminhoAumentante = []

    # Executa a busca em profundidade (DFS) para encontrar o caminho aumentante
    DFS(grafo, fonte, sumidouro, caminhoAumentante)

    print(f"\n\n\nCaminho aumentante: {caminhoAumentante}\n\n\n")

    return caminhoAumentante

#def find_augmenting_path_2(vertices, arestas, fonte, sumidouro):
    # Cria um dicionário para mapear os vértices por seus identificadores
    grafo = {vertice[0]: vertice for vertice in vertices}

    # Cria um dicionário para mapear os predecessores de cada vértice
    predecessores = {vertice[0]: None for vertice in vertices}

    # Cria um dicionário para armazenar o fluxo atual de cada aresta
    fluxoAtual = {(aresta[0], aresta[1]): aresta[2] for aresta in arestas}

    # Cria um dicionário para armazenar a capacidade residual de cada aresta
    capacidadeResidual = {(aresta[0], aresta[1]): aresta[3] for aresta in arestas}

    # Inicializa o caminho aumentante como uma lista vazia
    caminhoAumentante = []

    # Executa uma busca em largura (BFS) para encontrar o caminho aumentante
    fila = [fonte]
    visitados = {vertice[0]: False for vertice in vertices}
    visitados[fonte] = True

    while fila:
        verticeAtual = fila.pop(0)

        # Verifica se o vértice atual é o vértice de destino
        if verticeAtual == sumidouro:
            # Reconstrói o caminho aumentante a partir dos predecessores
            aresta = predecessores[verticeAtual]
            while aresta is not None:
                caminhoAumentante.append(aresta)
                aresta = predecessores[aresta[0]]
            break

        # Explora as arestas do vértice atual
        for aresta in arestas:
            if aresta[0] == verticeAtual and not visitados[aresta[1]] and capacidadeResidual[(aresta[0], aresta[1])] > 0:
                verticeAtual = aresta[1]
                fila.append(verticeAtual)
                visitados[verticeAtual] = True
                predecessores[verticeAtual] = aresta

    return caminhoAumentante

def minimun_flow(caminho):
    capacidadeResidual = 0
    for aresta in caminho:
        if aresta[2] < capacidadeResidual:
            capacidadeResidual = aresta[2]

    return capacidadeResidual

def maximun_flow(grafo, fonte):
    fluxoMaximo = 0
    for aresta in grafo[1]:
        if aresta[0] == fonte:
            fluxoMaximo += aresta[2]
    
    return fluxoMaximo

# retorna um fluxo maximo
def ford_fulkerson(grafo, s, t):
    aux = True
    for aresta in grafo[1]:
        aresta[2] = 0
    
    # suponho que como os fluxos estao zerados, existe no mínimo um caminho aumentante
    while aux:
        caminho = find_augmenting_path(grafo, s, t)
        capacidadeResidual = maximun_flow(caminho)

        for aresta in caminho:
            aresta[2] = aresta[2] + capacidadeResidual

        if len(caminho) == 0:
            aux = False
    
    return maximun_flow(grafo, s)

def main():
    grafo = [vertices, arestas]
    fluxoMaximo = ford_fulkerson(grafo, 's', 't')
main()
