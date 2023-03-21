# 15 * 5의 행렬을 구성(아무것도 없는 상태)
array = [[""] * 15 for _ in range(5)]

# 행렬 안에 행의 기준으로 단어를 입력
for i in range(5):
    s = input()
# 행에 들어간 문자의 순서대로 행의 왼쪽부터 행렬 구성
    for j in range(len(s)):
        array[i][j] = s[j]

# 세로로 출력
# 열을 기준으로 잡은 상태에서
for j in range(15):
# 행 순서대로
    for i in range(5):
# i,j가 빈칸이 아니라면
        if array[i][j] != '':
# (i, j)를 한 줄로 출력하면서 붙혀서 쓴다.
            print(array[i][j], end='')
    # print() <- 세로읽기를 하면서 각 열마다 칸을 구분짓고 싶을 때