# 100*100의 값이 0인 array 생성
array = [[0] * 100 for _ in range(100)]

# 색종이의 개수 입력, count값을 초기화
N = int(input())
count = 0

# 색종이 좌표에 대해 색종이 범윈만큼 1값 부여
for _ in range(N):
    a, b = map(int, input().split())
    for i in range(a, a + 10):
        for j in range(b, b + 10):
            array[i][j] = 1

# array의 범위 내에서 해당하는 array[i][j]가 1이라면 카운트에 1씩 추가
for i in range(len(array)):
    for j in range(len(array)):
        if array[i][j] == 1:
            count += 1
print(count)