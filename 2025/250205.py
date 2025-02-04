# 세로읽기 (10798번)

li = []
for i in range(5):
    n = input()
    li.append(n)

for j in range(15):
    for i in range(5):
        if j < len(li[i]):
            print(li[i][j], end='')
