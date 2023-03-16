import sys
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt


def draw_graph(graph, node_labels, edge_labels, title):
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=False, node_size=2000, node_color="skyblue", font_size=10, font_weight="bold")
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    nx.draw_networkx_labels(graph, pos, labels=node_labels)
    plt.title(title)
    plt.show()


def construct_building(T, test_cases):
    for _ in range(T):
        N, K, d, rules, W = test_cases[_]

        rule = [[] for _ in range(N + 1)]
        NTB = [0] * (N + 1)

        for X, Y in rules:
            rule[X].append(Y)
            NTB[Y] += 1

        queue = deque(i for i in range(1, N + 1) if NTB[i] == 0)

        Time = [0] * (N + 1)

        # Create a directed graph
        G = nx.DiGraph()
        for i in range(1, N + 1):
            G.add_node(i)
        for X, Y in rules:
            G.add_edge(X, Y)

        while queue:
            i = queue.popleft()
            Time[i] += d[i - 1]
            for j in rule[i]:
                NTB[j] -= 1
                if NTB[j] == 0:
                    queue.append(j)
                Time[j] = max(Time[j], Time[i])

        # Draw the final graph with the time to build W
        node_labels = {i: f'{i}, T: {Time[i]}' for i in G.nodes()}
        edge_labels = {(X, Y): f'{X} -> {Y}' for X, Y in rules}
        draw_graph(G, node_labels, edge_labels, f"Final Graph, Time to build W: {Time[W]}")

T = int(input())
test_cases = []

for _ in range(T):
    N, K = map(int, input().split())
    d = list(map(int, input().split()))
    rules = [tuple(map(int, input().split())) for _ in range(K)]
    W = int(input())
    test_cases.append((N, K, d, rules, W))

construct_building(T, test_cases)

