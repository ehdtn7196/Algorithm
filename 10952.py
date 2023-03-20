import sys

while True:
    try:
        A, B = map(int, sys.stdin.readline().rstrip().split())
        if 0 < A < 10 and 0 < B < 10:
            print(A + B)

    except EOFError:
        break