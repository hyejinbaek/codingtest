# 세탁소 사장 동혁 (2720번)

t = int(input())

for _ in range(t):
    c = int(input())
    for j in [25, 10, 5, 1]:
        print(c//j, end=' ')
        c = c%j