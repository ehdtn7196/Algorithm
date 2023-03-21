a = 0 # 학점의 총합
b = 0 # 학점 * 과목평점

for i in range(20):
    C, N, S = input().split()
    N = float(N)
    a += N
    if S == 'P':
        a -= N
        b -= N
    elif S == 'A+':
        N = N * 4.5
    elif S == 'A0':
        N = N * 4
    elif S == 'B+':
        N = N * 3.5
    elif S == 'B0':
        N = N * 3
    elif S == 'C+':
        N = N * 2.5
    elif S == 'C0':
        N = N * 2
    elif S == 'D+':
        N = N * 1.5
    elif S == 'D0':
        N = N * 1
    elif S == 'F':
        N = N * 0
    b += N
print(b/a)
