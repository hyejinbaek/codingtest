def step_2739():
    n = int(input())
    for i in range(1,10):
        print(n , "*", i, "=", n*i)

def step_10950():
    t = int(input())
    for _ in range(t):
        a,b = map(int, input().split())
        print(a+b)

def step_8393():
    n = int(input())
    sum = 0
    for i in range(n+1):
        sum = sum + i
    print(sum)

def step_25304():
    x = int(input())
    n = int(input())
    sum = 0
    for i in range(n):
        a, b = map(int, input().split())
        sum += a*b
    if x == sum:
        print("Yes")
    else:
        print("No")

def step_15552():
    import sys
    t = int(sys.stdin.readline())
    for i in range(t):
        a,b = map(int, sys.stdin.readline().split())
        print(a+b)

def step_11021():
    t = int(input())
    for i in range(1, t+1):
        a, b = map(int, input().split())
        print("Case #" + str(i) + ":", a+b)

        
if __name__ == '__main__':
   step_11021()