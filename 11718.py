while True:
    try:
        print(input())
    except EOFError:
        break

import sys
S = sys.stdin.readline
while True:
    try:
        N = S().strip()
        print(N)
    except EOFError:
        break