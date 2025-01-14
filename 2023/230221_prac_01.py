def step_11651():
    import sys
    n = int(sys.stdin.readline())
    num = []
    for i in range(n):
        num.append(list(map(int, sys.stdin.readline().split())))
    num.sort(key=lambda x:(x[1], x[0]))
    for i in num:
        print(i[0],i[1])

def step_1181():
    import sys
    n = int(sys.stdin.readline())
    num = []
    for i in range(n):
        num.append(sys.stdin.readline().strip())
    num_lst = set(num)
    lst = list(num_lst)
    lst.sort()
    lst.sort(key=len)
    for i in lst:
        print(i)

def step_10814():
    import sys
    n = int(sys.stdin.readline())
    member = []
    for i in range(n):
        member.append(list(sys.stdin.readline().split()))
    member.sort(key=lambda x: int(x[0]))
    print("member == ", member)
    for i in range(n):
        print(member[i][0], member[i][1])

def step_18870():
    import sys
    n = int(sys.stdin.readline())
    num = list(sys.stdin.readline().split())
    arr = []
    arr = list(sorted(set(num)))
    dic = {arr[i]: i for i in range (len(arr))}

    for i in num:
        print(dic[i],end=' ')

if __name__ == '__main__':
    step_18870()