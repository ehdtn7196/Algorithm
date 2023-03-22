N = int(input())
count = 0

A = list(map(int, input().split()))
for a in A:
    # 리스트 생성
    lst = []
    # A리스트 안의 원소 a에 대해서 1부터 a까지로 나누고 나머지가 0이면 a의 약수
    for i in range(1, a+1):
        if a % i == 0:
            lst.append(i)
    # 리스트의 길이가 2라면 약수가 1과 자기자신이므로 count에 1추가
    if len(lst) == 2:
        count += 1

print(count)