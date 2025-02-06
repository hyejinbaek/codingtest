# 진법 변환 (2745번)

n, b  = input().split()
li = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n = n[::-1]
res = 0

for i, n in enumerate(n):
    res += (int(b)**i)*(li.index(n))
print(res)