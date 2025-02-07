# 진법 변환 2 (11005번)

n, b = map(int, input().split())
li = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

s = ''

while n:
    s+=str(li[n%b])
    print(s)
    n //= b
    
print(s[::-1])