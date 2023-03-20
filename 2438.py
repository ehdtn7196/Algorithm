N = int(input())
if 1 <= N <= 100:
    for i in range(1, N+1):
        star = ''
        space = ''
        for j in range(N-i):
            space += ' '
        for k in range(i):
            star += '*'
        print(space + star)