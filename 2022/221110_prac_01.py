# (p.86) 그리디 알고리즘
# 거스름돈
n = 1260
count = 0


coint_types = [500, 100, 50, 10]

for coin in coint_types:
    count += n // coin
    print(count)
    n %= coin
    print("==n==",n)

print(coin)