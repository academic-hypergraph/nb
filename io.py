# -*- coding: utf-8 -*-
"""io.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Fq3fC3wjjHfJZEWnODZajGV8OfIcEDbX
"""

import networkx as nx
import matplotlib.pyplot as plt

# Definir as hiperarestas do hipergrafo para NCA e SEM
hyperedges = [
    ("Coleta de Dados", "Identificação de Condições Necessárias", "NCA"),
    ("NCA", "Especificação de Modelo", "SEM"),
    ("Especificação de Modelo", "Avaliação de Ajuste", "SEM"),
    ("Avaliação de Ajuste", "Interpretação de Resultados", "Publicação Acadêmica"),
    # Adicione outras etapas conforme necessário
]

# Função para criar e desenhar o hipergrafo direcionado
def draw_academic_hypergraph(hyperedges):
    G = nx.DiGraph()

    # Extrair nós únicos das hiperarestas
    nodes = set()
    for edge in hyperedges:
        nodes.update(edge)

    # Adicionar nós ao grafo
    G.add_nodes_from(nodes)

    # Adicionar hiperarestas direcionadas ao grafo
    for edge in hyperedges:
        source = edge[0]
        for target in edge[1:]:
            G.add_edge(source, target)

    # Definir o layout do grafo com espaçamento acadêmico
    pos = nx.spring_layout(G, seed=42, k=0.8)

    # Desenhar os nós
    nx.draw_networkx_nodes(G, pos, node_size=1500, node_color="lightblue")

    # Desenhar as arestas direcionadas
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), width=1, edge_color="gray", arrowsize=20)

    # Adicionar rótulos aos nós
    nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif")

    # Ajustar o tamanho da figura
    plt.figure(figsize=(12.8, 7.2))

    # Mostrar a visualização
    plt.title("Hipergrafo Acadêmico: NCA e SEM")
    plt.axis("off")
    plt.tight_layout()
    plt.show()

# Executar a função para desenhar o hipergrafo
if __name__ == "__main__":
    draw_academic_hypergraph(hyperedges)