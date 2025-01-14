def step_10810():
    n, m = map(int, input().split())
    nn = [0]*n

    for _ in range(m):
        i, j, k = map(int, input().split())
        for idx in range(i, j+1):
            print("idx ===", idx)
            nn[idx-1]=k

    for i in range(n):
        print(nn[i], end = ' ')

def step_10813():
    n, m=map(int, input().split())
    box = [i for i in range(1,n+1)]

    for _ in range(m):
        i, j = map(int, input().split())
        temp = box[i-1]
        box[i-1]=box[j-1]
        box[j-1]=temp

    for b in box:
        print(b, end=' ')

def step_10811():
    n, m = map(int, input().split())
    lst = [i for i in range(1, n+1)]

    for _ in range(m):
        i, j = map(int, input().split())
        r = j - i + 1
        for _ in range(r//2):
            tmp = lst[i-1]
            lst[i-1]=lst[j-1]
            lst[j-1]=tmp
            i += 1
            j -= 1

    for jj in lst:
        print(jj, end = ' ')


if __name__ == '__main__':
    step_10811()