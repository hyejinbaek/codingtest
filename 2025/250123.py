# 별 찍기(2444번)

n = int(input())

# 홀수 갯수로 증가(1,3,5,7,9)
for i in range(1, n):
    print(' '*(n-i) + '*' * (2*i-1))

# 홀수 갯수로 감소
for i in range(n, 0, -1):
    print(' '*(n-i) + '*' * (2*i-1))