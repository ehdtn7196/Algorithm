import math

MAX_VALUE = 10000

T = int(input())

for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    if any(val > MAX_VALUE for val in [x1, y1, x2, y2]) or r1 < 0 or r2 < 0 or r1 > MAX_VALUE or r2 > MAX_VALUE:
        continue

    d = math.sqrt((x2-x1)**2 + (y2-y1)**2)

    if abs(r1-r2) < d < r1 + r2:
        print(2)
    elif d == r1+r2 or d == abs(r1-r2):
        if d == 0 and r1 == r2:
            print(-1)
        else:
            print(1)
    else:
        print(0)