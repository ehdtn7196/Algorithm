import sys
from collections import deque


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
        while queue:
            i = queue.popleft()
            Time[i] += d[i - 1]
            for j in rule[i]:
                NTB[j] -= 1
                if NTB[j] == 0:
                    queue.append(j)
                Time[j] = max(Time[j], Time[i])
        print(Time[W])


T = int(sys.stdin.readline())
test_cases = []
for _ in range(T):
    N, K = map(int, sys.stdin.readline().split())
    d = list(map(int, sys.stdin.readline().split()))
    rules = [tuple(map(int, sys.stdin.readline().split())) for _ in range(K)]
    W = int(sys.stdin.readline())
    test_cases.append((N, K, d, rules, W))

construct_building(T, test_cases)