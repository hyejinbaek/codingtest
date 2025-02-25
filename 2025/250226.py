# 숫자 카드 2 (10816번)

import sys

n = int(sys.stdin.readline().strip())
n_li = list(map(int, sys.stdin.readline().strip().split()))

m = int(sys.stdin.readline().strip())
m_li = list(map(int, sys.stdin.readline().strip().split()))


n_li.sort()

dic = {}

for x in n_li:
    if x in dic:
        dic[x] += 1
    else:
        dic[x] = 1
print(dic)

for x in m_li:
    if x in dic:
        print(dic[x], end = ' ')
    else:
        print('0', end = ' ')