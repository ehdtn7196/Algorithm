blank = ' '
star = '*'
N = int(input())
for i in range(1, (N * 2)):
    print(blank * abs(N - i) + star * (2 * (N - abs(N - i)) - 1))