def fibonacci(n, a=1, b=0):

    if n == 0:
        return b
    else:
        return fibonacci(n-1, b, a+b)

T = int(input())

for _ in range(T):
    n = int(input())
    if 0 <= n <= 40:
        a, b = 1, 0
        for _ in range(n):
            a, b = b , a+b
    print(a, b)
else:
    pass