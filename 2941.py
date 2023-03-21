croatialist = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()
count = 0
i = 0
while i < len(word):
    if word[i:i+2] in croatialist:
        count += 1
        i += 2
    elif i < len(word)-2 and word[i:i+3] in croatialist:
        count += 1
        i += 3
    else:
        count += 1
        i += 1
print(count)

#2번째 풀이
croatialist = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()
count = 0

for i in croatialist:
    count += word.count(i)
    word = word.replace(i, ' ')

string = word.replace(' ', '')
count += len(string)
print(count)