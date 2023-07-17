# Universidade Federal do Ceará - campus Crateús
# Ciência da computação - Algoritmos em Grafos 2023.1
# Aguiar - 495586 

# Esse algoritmo opera sobre um grafo ponderado, não dirigido e não contém ciclos negativos. 
# Seu objetivo é encontrar uma arvore geradora mínima com o algoritmo de Kruskal.

# cada vertice tem ['seu identificador', 'seu representante da componente']
# entao um vertice vai estar e uma componente e terá esse atributo setado
vertices = [['a', 'h'], ['b', 'h'], ['c', 'h'], ['d', 'h'], ['e', 'h'], ['f', 'h'], ['g', 'h'], ['h', 'h'], ['i', 'h']]

# cada aresta tem ('vertice saida', 'vertice chegada', peso)
arestas = [
    ('a', 'b', 4),
    ('a', 'h', 8),
    ('b', 'h', 11),
    ('b', 'c', 8),
    ('c', 'i', 2),
    ('c', 'd', 7),
    ('c', 'f', 4),
    ('d', 'f', 14),
    ('d', 'e', 9),
    ('e', 'f', 10),
    ('g', 'f', 2),
    ('g', 'i', 6),
    ('g', 'h', 1),
    ('h', 'i', 7),
]

# retorna o array de arestas ordenado com base no peso
def Order_Edges(arestas):
    arestas_ordenadas = sorted(arestas, key=lambda x: (x[2], x[0], x[1]))
    return arestas_ordenadas

# retorna o vértice com o ele sendo seu proprio representante
def Make_Set(vertice):
    vertice[1] = vertice[0]
    return vertice

# retorna true se ambos os vertices da aresta estiverem o mesmo representante
def Find_Set(vertices, aresta):
    vertice_u = []
    vertice_v = []

    # percorre os vertices procurando u e v
    for vertice in vertices:
        if vertice[0] == aresta[0] or vertice[0] == aresta[1]:
            if len(vertice_u) == 0:
                vertice_u = vertice
            else:
                vertice_v = vertice

            if len(vertice_u) == 2 and len(vertice_v) == 2 and vertice_u[1] == vertice_v[1]:
                return True
    
    return False

# une as componentes de u e v, criterior de união é que a componente maior recebe a menor 
def Union(vertices, aresta):
    u, v = aresta[0], aresta[1]
    u_representante, v_representante = None, None

    # encontra representantes de u e v
    for vertice in vertices:
        if vertice[0] == u:
            u_representante = vertice[1]
        elif vertice[0] == v:
            v_representante = vertice[1]

    # verifica se os representantes são diferentes
    if u_representante != v_representante:
        for i, vertice in enumerate(vertices):
            if vertice[1] == u_representante:
                vertices[i] = [vertice[0], v_representante]

    return vertices

# implementação mais proxima possivel de kruskal, dada no livro
def MST_Kruskal(grafo):
    MST = [[], []]

    for vertice in grafo[0]:
        MST[0].append(Make_Set(vertice))

    arestasOrdenadas = Order_Edges(grafo[1])

    for aresta in arestasOrdenadas:
        if not Find_Set(MST[0], aresta):
            MST[1].append(aresta)
            MST[0] = Union(MST[0], aresta)

    return MST

def main():
    grafo = [vertices, arestas]
    grafo = MST_Kruskal(grafo)

    print(f"\n===== Arvore geradora minima =====")
    print(f"G.V = {grafo[0]}")
    print(f"G.E = {grafo[1]}\n")
main()
