
# 테스트 케이스의 수
T = int(input())

for _ in range(T):
    # 건물의 개수와 건물 간의 규칙 개수를 입력받기
    N, K = map(int, input().split())

    # 각 건물에 대한 소요시간 입력받기
    d = list(map(int, input().split()))

    rule = [[] for _ in range(N + 1)] # 각 건물에 해당하는 인덱스 추가, rule : N번째 까지의 리스트
    NTBN = [0] * (N + 1) # N건물이 건설되어야 하는 데 필요한 건물의 수(1부터 N까지)

    # X, Y 의 값을 입력받기
    for i in range(K):
        X, Y = map(int, input().split())

        rule[X].append(Y)  # 규칙 : X를 완성해야 Y를 시작할 수 있다.
        NTBN[Y] += 1 #Y에 X경로가 필요하므로 +1

    # 완성 시켜야 할 건물 번호 리스트
    MTB = []
    for i in range(1, N + 1):
        if NTBN[i] == 0 : # i 건물이 건설되어야 하는 데 필요한 건물의 수가 0(즉 시작 가능한 건물)
            MTB.append(i) # MUST TO BUILD는 i부터 시작되면 된다

    # N번째 건물을 완성하는데 필요한 최소 시간
    Time = [0] * (N + 1)
    for i in MTB:
        Time[i] = d[i - 1] #Time 함수의 i는 건물 소요시간 리스트에 있는 i번째 상수

    # W번째 건물까지의 최소 소요시간 구하기
    W = int(input())
    for i in MTB:
        if i == W:
            print(Time[i])
            break

        for j in rule[i]:
            Time[j] = max(Time[j], Time[i] + d[j-1])
            # i 소요시간 + j 소요시간, 이미 j 소요시간이 있으면 더 큰 값으로 갱신
            NTBN[j] -= 1
            # j 건물까지 가기 위한 건물 1개 감소
            if NTBN[j] == 0:
            # j 이전에 지을것이 없다면
                MTB.append(j)
                # j가 시작지점
        if i == W:
            print(Time[i])
            break