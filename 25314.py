N = int(input())
if 4 <= N <= 1000 and N % 4 == 0:
    name = ''
    for i in range(N // 4):
        name += 'long '
    print(name + 'int')