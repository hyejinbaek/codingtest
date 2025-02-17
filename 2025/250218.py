# 체스판 다시 칠하기 (1018번)

n, m = map(int, input().split())

li = []
cnt = []

for i in range(n):
    li.append(input())
    
for a in range(n-7):
    for b in range(m-7):
        w_ind = 0
        b_ind = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if li[i][j]!='W':
                        w_ind += 1
                    else:
                        b_ind += 1
                else:
                    if li[i][j] != 'W':
                        b_ind += 1
                    else:
                        w_ind += 1
                        
        cnt.append(w_ind)
        cnt.append(b_ind)
print(min(cnt))