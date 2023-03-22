N, K = map(int, input().split())
lst = []

# 1부터 N까지 N을 i로 나눴을 때 나머지가 0이라면
# 그 수는 N의 약수, lst라는 리스트에 그 수 추가
for i in range(1, N+1):
    if N % i == 0:
        lst.append(i)
# lst의 길이 즉 약수의 개수가 K보다 크거나 같다면
# k번째의 약수를 출력
if len(lst) >= K:
    print(lst[K-1])
# 약수의 개수가 K보다 크거나 같지 않으면 0
else:
    print(0)