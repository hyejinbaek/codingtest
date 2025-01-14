def step_2750():
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(int(input()))
    arr = sorted(arr)
    for i in range(len(arr)):
        print(arr[i])

def step_2587():
    arr = []
    for i in range(5):
        arr.append(int(input()))
    arr.sort()
    print(int(sum(arr)/5))
    print(arr[2])

def step_25305():
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    print(sorted(x)[-k])

def step_2751():
    import sys

    n = int(input())
    num = []
    for _ in range(n):
        num.append(int(sys.stdin.readline()))

    num.sort()

    for i in num:
        print(i)

if __name__ == '__main__':
    step_2751()