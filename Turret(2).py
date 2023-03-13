import math

# 상수 정의
MAX_COORDINATE = 10000
NO_INTERSECTION = 0
ONE_INTERSECTION = 1
TWO_INTERSECTIONS = 2

# 두 점 사이 거리 계산하는 함수
def calc_distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

# 좌표, 반지름 값 검사 함수
def is_valid_input(x1, y1, r1, x2, y2, r2):
    if any(val > MAX_COORDINATE for val in [x1, y1, x2, y2]) or r1 < 0 or r2 < 0:
        return False
    return True

# 두 원의 교차 여부 계산 함수
def calc_circle_intersection(x1, y1, r1, x2, y2, r2):
    d = calc_distance(x1, y1, x2, y2)
    if d == 0 and r1 == r2:
        return -1
    elif abs(r1-r2) < d < r1 + r2:
        return TWO_INTERSECTIONS
    elif d == r1+r2 or d == abs(r1-r2):
        return ONE_INTERSECTION
    else:
        return NO_INTERSECTION

# 테스트 케이스 처리
def process_test_case():
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    if not is_valid_input(x1, y1, r1, x2, y2, r2):
        return

    intersection_count = calc_circle_intersection(x1, y1, r1, x2, y2, r2)
    print(intersection_count)

# 메인 코드
T = int(input())

for i in range(T):
    process_test_case()