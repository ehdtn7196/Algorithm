n = int(input())

if n <= 40:
    def fibonacci(n, a=1, b=0):
        if n == 0:
            return b
        else:
            return fibonacci(n-1, b, a+b)

    print(fibonacci(n))