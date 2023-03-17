# input R, C, M (Row, Col, sharks)
R, C, M = map(int, input().split())

# check R, C, M range
if not (2 <= R <= 100) or not (2 <= C <= 100) or not (0 <= M <= R * C):
    exit()

# creat R, C array
array = [[(0, 0, 0) for j in range(C+1)] for i in range(R+1)]

# input shark's information
for k in range(M):
    r, c, s, d, z = map(int, input().split())

    # Check the constraints for r, c, s, d, z
    if not (1 <= r <= R) or not (1 <= c <= C) or not (0 <= s <= 1000) or not (1 <= d <= 4) or not (1 <= z <= 10000):
        exit()

    array[r][c] = (s, d, z)        # value of (r, c) is z

# catch shark in every sec
catch = 0
for j in range(1, C+1):
    for i in range(1, R+1):
        if not array[i][j] == (0, 0, 0):
            catch += array[i][j][2]
            array[i][j] = (0, 0, 0)
            break
# move shark
    new_array = [[(0, 0, 0) for _ in range(C+1)] for _ in range(R+1)]
    for r in range(1, R+1):
        for c in range(1, C+1):
            if not array[r][c] == (0, 0, 0):
                s, d, z = array[r][c]
                new_r, new_c = r, c

                for _ in range(s % (2 * (R - 1)) if d == 1 or d == 2 else s % (2 * (C - 1))):
                    if d == 1 or d == 2:
                        if new_r == 1:
                            d = 2
                        elif new_r == R:
                            d = 1
                        new_r += -1 if d == 1 else 1
                    else:
                        if new_c == 1:
                            d = 3
                        elif new_c == C:
                            d = 4
                        new_c += -1 if d == 4 else 1
                # if two shark in same space
                if new_array[new_r][new_c] == (0, 0 ,0) or new_array[new_r][new_c][2] < z:
                    new_array[new_r][new_c] = (s, d, z)
    array = new_array

print(catch)