# 영화감독 숌 (1436번)
'''
1   - 666
2   - 1666
3   - 2666
..
187 - 66666
500 - 166699

'''

n = int(input())

i = 0
res = 666

while True:
    if '666' in str(res):
        i += 1
        print("== 666",i)
    if i == n:
        break
    
    res += 1
    print("=== res",res)

print(res)