N, X = map(int, input().split())
A = list(map(int, input().split()))
if 1 <= N <= 10000 and 1 <= X <= 10000:
    print(*[num for num in A if num < X])