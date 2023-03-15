def is_valid_input(n, k, d, rules, w):
    if not (2 <= n <= 1000 and 1 <= k <= 100000):
        return False
    if not all(0 <= di <= 100000 for di in d):
        return False
    if not all(1 <= x <= n and 1 <= y <= n for x, y in rules):
        return False
    if not (1 <= w <= n):
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
    MTB = []
    for i in range(1, N + 1):

        # i 건물이 건설되어야 하는 데 필요한 건물의 수가 0(즉 시작 가능한 건물)
         if NTB[i] == 0:
            # MUST TO BUILD는 NEED TO BUILD list의 i번째부터 시작하면 된다
                MTB.append(i)

    # N번째 건물을 완성하는데 필요한 최소 시간
    Time = [0] * (N + 1)
    for i in MTB:
        # Time 함수의 i번째 인덱스는 건물 소요시간 리스트에 있는 i번째 상수
        Time[i] = d[i - 1]

    # W번째 건물까지의 최소 소요시간 구하기
    W = int(input())

    #MTB 함수 안에서의 i가 W와 같다면 Time 함수 안의 i에 해당하는 리스트를 가져오면 최소시간이다.
    for i in MTB:
        if i == W:
            print(Time[i])
            break

    # i라는 상수 안에서의 j의 상관관계, j로 갈때의 시간이
        for j in rule[i]:
            Time[j] = max(Time[j], Time[i] + d[j-1])
        # i 소요시간 + j 소요시간, 이미 j 소요시간이 있으면 더 큰 값으로 갱신
            NTB[j] -= 1
        # j 건물까지 가기 위한 건물 1개 감소
            if NTB[j] == 0:
        # j 이전에 지을것이 없다면
                MTB.append(j)
            # j가 시작지점


#이 코드는 위상 정렬을 이용해 건물을 짓는 순서를 결정하고, 각 건물을 짓는 최소 시간을 계산하는 함수입니다.
#이 코드에서 가장 큰 문제는, 반복문이 중첩되어서 모든 건물에 대해서 여러 번 반복하게 된다는 것입니다.
# 이 때문에 계산량이 증가하여 연산이 너무 비효율적이 됩니다.
#예를 들어, 건물의 개수가 1000개인 경우, 건물 간의 규칙이 모두 연결되어 있는 경우, 건물 하나를 짓기 위해 필요한 모든 건물을 확인해야 하므로,
#최악의 경우 건물을 짓는 시간이 O(1000^2)만큼 소요될 수 있습니다.
#따라서 이 코드를 개선하기 위해서는, 건물을 짓는 순서를 결정하는 위상 정렬 과정에서, 모든 건물을 반복하지 않고 필요한 건물만을 선택하도록 개선하는 것이 필요합니다.
#이를 위해서는, 위상 정렬 알고리즘을 적용할 때 큐(Queue)를 사용하여 필요한 건물만을 처리하도록 구현하는 것이 좋습니다.
