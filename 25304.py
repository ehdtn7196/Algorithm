X = int(input())
N = int(input())
total = 0
for i in range(N):
    a, b = map(int, input().split())
    if 1 <= X <= 1000000000 and 1 <= N <= 100 and 1 <= a <= 1000000 and 1 <= b <= 10:
        total += a * b
        if total == X:
            break
if total == X:
    print('Yes')
else:
    print('No')