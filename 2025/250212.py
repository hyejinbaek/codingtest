# 배수와 약수 (5086번)

while(1):
    n, m = map(int, input().split())
    if n == 0 and m ==0:
        break
    if n<m and m%n == 0:
        print("factor")
    elif n>m and n%m == 0:
        print("multiple")
    else:
        print("neither")