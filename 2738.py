# 행렬의 크기 입력받기
N, M = map(int, input().split())

# M*N 행렬 3개 생성하기
A = [[0] * M for _ in range(N)]
B = [[0] * M for _ in range(N)]
C = [[0] * M for _ in range(N)]

# A 행렬 입력받기
for i in range(N):
    A[i] = list(map(int, input().split()))

# B 행렬 입력받기
for i in range(N):
    B[i] = list(map(int, input().split()))

# A + B 값을 C에 저장하기
for i in range(N):
    for j in range(M):
        C[i][j] = A[i][j] + B[i][j]

for r in C:
    print(*r)

    print(r)