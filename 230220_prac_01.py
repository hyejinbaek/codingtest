def step_2751():
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(int(input()))
    arr.sort()
    for i in range(n):
        print(arr[i])

def step_2108():
    import sys
    from collections import Counter
    n = int(sys.stdin.readline())
    num = []
    for _ in range(n):
        num.append(int(sys.stdin.readline()))
        
    print(round(sum(num)/n))
    num.sort()
    print("num === ", num)
    print(num[n//2])

    cnt_num = Counter(num).most_common()
    print("cnt_num === ", cnt_num)
    print("cnt_num 0 1 === ",cnt_num[0][1])
    print("cnt_num 1 1 === ",cnt_num[1][1])
    if len(cnt_num) > 1 and cnt_num[0][1] == cnt_num[1][1]:
        print(cnt_num[1][0])
    else:
        print(cnt_num[0][0])

    print(max(num)-min(num))

def step_1427():
    n = list(map(int, str(input())))
    n.sort(reverse = True)
    for i in n:
        print(i, end='')

def step_11650():
    import sys
    n = int(sys.stdin.readline())
    num = []
    for i in range(n):
        num.append(list(map(int, sys.stdin.readline().split())))
    num.sort(key=lambda x:(x[0], x[1]))
    for i in num:
        print(i[0],i[1])
    

if __name__ == '__main__':
    step_11650()