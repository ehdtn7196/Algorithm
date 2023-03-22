lst = []

while True:
    # n = -1 이 될 때 까지 코드 반복
    n = int(input())
    if n == -1 or not(2 < n < 100000):
        break

    # 1부터 n까지 나누어 떨어지면 약수 리스트에 추가
    for i in range(1, n+1):
        if n % i == 0:
            lst.append(i)
    # 만약 약수들의 합이 n과 같으면
    if sum(lst[:-1]) == n:
        print(str(n) + ' = ', end='')
        # 자기자신을 제외한 약수들까지
        for j in lst[:-1]:
            # 가장 큰 약수이면
            if j == lst[-2]:
                print(str(j))
            # 가장 큰 약수 전까지는 "a + "이런 식으로 출력
            else:
                print(str(j) + ' + ', end='')
    # 약수들의 합이 n과 같지 않다면
    else:
        print(n, end=' is NOT perfect.')
    # 리스트 초기화
    lst = []