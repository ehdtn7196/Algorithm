# 입력받은 점수의 평균을 구하는 식
def average(sc, a):
    return sum(sc) / a

# 몇 퍼센트의 학생들이 점수를 넘었는지에 대한 식
def avgup(a, b):
    return format((a / b) * 100, ".3f")
    # return format((a // b) * 100, ".3f")
    # 몫만 구해서 100으로 곱한 값이라 계속 0이 출력
# 테스트 케이스
T = int(input())

# 메인 코드
for i in range(T):
    N, *score = map(int, input().split())
    avg = average(score, N)
    total = 0
    for s in score:
        if s > avg:
            total += 1
        else:
            total += 0
    ans = avgup(total, N)
    print(ans + '%')