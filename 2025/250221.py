# 문자열 집합 (14425번)

n, m = map(int, input().split())

n_list = set()
count = 0
for i in range(n):
    n_list.add(input())
    
for q in range(m):
    li = input()
    if li in n_list:
        count += 1
        
print(count)