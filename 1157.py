# 1
# 입력되는 모든 문자들을 대문자로 저장
N = input().upper()
# 딕셔너리 생성
dict_lst = {}
# N에 존재하는 char에 대해서
for char in N:
# char가 딕셔너리에 존재한다면
    if char in dict_lst:
# 딕셔너리 안의 char라는 key에 해당하는 value값을 1 증가
        dict_lst[char] += 1
# char가 딕셔너리에 존재하지 않았다면 그 value = 1
    else:
        dict_lst[char] = 1
# 딕셔너리에서 얻어진 key들 중 가장 큰 value를 가지고 있는 key
most = max(dict_lst, key=dict_lst.get)
# 가장 큰 value를 가진 key들이 여러개라면
if list(dict_lst.values()).count(dict_lst[most]) > 1:
    print('?')
else:
    print(most)

# 2
N = input().upper()
dict_lst = {}
for char in N:
    if char in dict_lst:
        dict_lst[char] += 1
    else:
        dict_lst[char] = 1
most = max(dict_lst, key=dict_lst.get)
if dict_lst[most] > 1:
    count = 0
    for val in dict_lst.values():
        if val == dict_lst[most]:
            count += 1
    if count > 1:
        print('?')
    else:
        print(most)
else:
    print(most)