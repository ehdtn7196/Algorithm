# 9*9 행렬 생성
array = [[0] * 9 for _ in range(9)]

# 숫자 입력 받기
for i in range(9):
    row = input().split()
    for j in range(9):
        array[i][j] = int(row[j])

# 최댓값과 최댓값이 위치한 행렬의 초기 위치값을 0으로 설정
max_num = 0
max_i, max_j = 0, 0
# 각 9개의 행을 9개의 열의 순서로 비교하면서 max_num과 max_i,j의 값을 갱신
for i in range(9):
    for j in range(9):
        if array[i][j] > max_num:
            max_num = array[i][j]
            max_i, max_j = i, j

print(max_num)
print(max_i+1, max_j+1)