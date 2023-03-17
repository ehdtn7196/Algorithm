A, B, C = map(int, input().split())
if A == B and B == C:
    print(10000 + A * 1000)
elif A == B and B != C or A == C and A != B:
    print(1000 + A * 100)
elif B == C and A != B:
    print(1000 + B * 100)
else:
    if A > B and A > C:
        print(A * 100)
    elif B > A and B > C:
        print(B * 100)
    elif C > A and C > B:
        print(C * 100)

A, B, C = map(int, input().split())

if A == B == C:
    print(10000 + A * 1000)
elif A == B or A == C:
    print(1000 + A * 100)
elif B == C:
    print(1000 + B * 100)
else:
    print(max(A, B, C) * 100)