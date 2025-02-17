# 수학은 비대면강의입니다 (19532번)
'''
완전탐색 : Brute Force algorithm(브루트포스 알고리즘)

문제를 해결하기 위해 모든 경우를 탐색하고 답을 도출하는 알고리즘 (결과를 찾는 것에 중점을 둠)

'''

a, b, c, d, e, f = map(int, input().split())

for i in range(-999, 1000):
    for j in range(-999, 1000):
        if (a*i) + (b*j) == c and (d*i) + (e*j) == f:
            print(i,j)