n = int(input())
if 1 <= n <= 10000:
    N = n * (n + 1) // 2
    print(N)

n = int(input())
if 1 <= n <= 10000:
    N = 0
    for i in range(1, n+1):
        N += i
    print(N)

