lst = []
for i in range(28):
    st = int(input())
    lst.append(st)
    total = list(range(1, 31))
who = list(set(total) - set(lst))
min_who = min(who)
max_who = max(who)
print(min_who)
print(max_who)