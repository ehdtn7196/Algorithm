import math

# 상수 정의
MAX_COORDINATE = 1000
NO_INTERSECTION = 0
ONE_INTERSECTION = 1

# 두 점과 원 사이 거리 계산하는 함수
def calc_intersection(x1, y1, x2, y2, cx, cy, r):

    d1 = math.sqrt((x1 - cx)**2 + (y1 - cy)**2)
    d2 = math.sqrt((x2 - cx)**2 + (y2 - cy)**2)

    if d1 < r < d2 or d2 < r < d1:
        return ONE_INTERSECTION
    else:
        return NO_INTERSECTION

# 좌표, 반지름 값 검사 함수
def is_valid_input(x1, y1, x2, y2, cx, cy, r, n):
    if any(val > MAX_COORDINATE for val in [x1, y1, x2, y2, cx, cy]) or r < 1 or r > 1000 or n < 1 or n > 50:
        return False
    return True


# 테스트 케이스 처리
def process_test_case():
    #x1, y1, x2, y2의 좌표를 입력받기
    x1, y1, x2, y2 = map(int, input().split())

    #원의 개수를 입력받기
    n = int(input())

    # 초기 출력 값
    total_intersection = 0

    #n개의 원에 대한 좌표, 반지름 입력하기
    for i in range(n):
        cx, cy, r = map(int, input().split())

        # 좌표, 반지름 값 검사하기
        if not is_valid_input(x1, y1, x2, y2, cx, cy, r, n):
            return

        #두 점과 원의 교차 여부를 판별하기
        intersection = calc_intersection(x1, y1, x2, y2, cx, cy, r)

        # 교차한 원이 있으면 출력 값에 1 추가
        if intersection == ONE_INTERSECTION:
            total_intersection += 1

        # 결과
    print(total_intersection)

# 테스트 케이스 개수 입력하기
T = int(input())

# 각 테스트 케이스 처리하기
for i in range(T):
    process_test_case()