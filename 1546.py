T = int(input())

for i in range(T):
    try:
        score = list(map(int, input().split()))
        M = max(score)
        new_score = [(s / M) * 100 for s in score]
        print(sum(new_score) / len(new_score))
    except:
        break