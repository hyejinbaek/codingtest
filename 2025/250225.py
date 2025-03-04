# 나는야 포켓몬 마스터 이다솜 (1620번)
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

dict = {}
for i in range(1, n + 1):
    a = input().rstrip()
    dict[i] = a
    dict[a] = i

for i in range(m):
    quest = input().rstrip()
    if quest.isdigit():
        print(dict[int(quest)])
    else:
        print(dict[quest])