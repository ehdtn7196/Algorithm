from queue import Queue

def is_valid_input(N, K, d, W):
    if not (2 <= N <= 1000 and 1 <= K <= 100000):
        return False
    if not all(0 <= di <= 100000 for di in d):
        return False
    if not all(1 <= X <= N and 1 <= Y <= N):
        return False
    if not (1 <= W <= N):
        return False
    return True

# 테스트 케이스의 수
T = int(input())

for _ in range(T):
    # 건물의 개수와 건물 간의 규칙 개수를 입력받기
    N, K = map(int, input().split())

    # 각 건물에 대한 소요시간 입력받기
    d = list(map(int, input().split()))

    # 각 건물에 해당하는 인덱스 추가, rule : N번째 까지의 리스트
    rule = [[] for _ in range(N + 1)]

    # N건물이 건설되어야 하는 데 필요한 건물의 수(1부터 N까지)
    NTB = [0] * (N + 1)

    # X, Y 의 값을 입력받기
    for i in range(K):
        X, Y = map(int, input().split())
        # 규칙 : X를 완성해야 Y를 시작할 수 있다.
        rule[X].append(Y)
        # Y에 X경로가 필요하므로 +1
        NTB[Y] += 1

    # 완성 시켜야 할 건물 번호 리스트
    MTB = Queue()
    for i in range(1, N + 1):
        # i 건물이 건설되어야 하는 데 필요한 건물의 수가 0(즉 시작 가능한 건물)
        if NTB[i] == 0:
            # MUST TO BUILD는 NEED TO BUILD list의 i번째부터 시작하면 된다
            MTB.put(i)

    # N번째 건물을 완성하는데 필요한 최소 시간
    Time = [0] * (N + 1)
    while not MTB.empty():
        # 큐에서 건물 하나를 빼서 처리
        i = MTB.get()
        # Time 함수의 i번째 인덱스는 건물 소요시간 리스트에 있는 i번째 상수
        Time[i] += d[i - 1]
        for j in rule[i]:
            NTB[j] -= 1
            if NTB[j] == 0:
                MTB.put(j)
            Time[j] = max(Time[j], Time[i])

    # 건물 W를 완성하는데 필요한 최소 시간을 출력합니다.
    W = int(input())
    print(Time[W])
