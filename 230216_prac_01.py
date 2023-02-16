def step_2738():
    import sys
    input = sys.stdin.readline
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    b = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(m):
            a[i][j] += b[i][j]
    for i in a:
        print(*i)

def step_2566():
    import sys
    input = sys.stdin.readline
    a = []
    for _ in range(9):
        a.append(list(map(int, input().split())))
    x = 0
    y = 0
    max = -1
    for i in range(9):
        for j in range(9):
            if a[i][j] > max:
                max = a[i][j]
                x = i+1
                y = j+1
    print(max)
    print(x, y)    

def step_2563():
    n = int(input())
    array = [[0] * 100 for _ in range(100)]
    for _ in range(n):
        y1, x1 = map(int, input().split())

        for i in range(x1, x1 + 10):
            for j in range(y1, y1 + 10):
                array[i][j] = 1

    result = 0
    for k in range(100):
        result += array[k].count(1)

    print(result)

if __name__ == '__main__':
    step_2563()