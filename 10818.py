N = int(input())
if 1 <= N <= 1000000:
    X = list(map(int, input().split()))
    if all(-100000 <= a <= 100000 for a in X):
        print(min(X), max(X))