T = int(input())

group_word = 0

for _ in range(T):
    word = input()
    result = 0
    # 인덱스 범위 생성 : 리스트 0번부터 (단어의 길이-1)까지 - 단어의 원소 개수만큼
    for i in range(len(word) - 1):
        # i번째 단어가 i+1번째 단어가 아니라면
        if word[i] != word[i+1]:
            # i+1번째 단어부터는 새로운 단어
            new_word = word[i+1:]
            # 새로운 단어가 이전에 word[i]에서 존재했었다면
            if new_word.count(word[i]) > 0:
                result += 1
                # 결과값에 1씩 증가
    if result == 0:
        group_word += 1
        # 결과가 0이라면 그룹단어
print(group_word)