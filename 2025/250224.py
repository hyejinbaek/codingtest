# 회사에 있는 사람 (7785번)

n = int(input())

li = set()
for _ in range(n):
    per, stats = input().split()
    if stats == "enter":
        li.add(per)

    else:
        li.remove(per)


for name in sorted(li, reverse=True):
    print(name)