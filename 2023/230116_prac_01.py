def step_11022():
    t = int(input())
    for i in range(1, t+1):
        a,b=map(int, input().split())
        print(f'Case #{i}:{a}+{b}={a+b}')

def step_2438():
    star = int(input())
    for i in range(1,star+1):
        print("*"*i)

def step_2439():
    star = int(input())
    for i in range(1, star+1):
        print(" "*(star-i) + "*"*i)

def step_10952():
    while 1:
        a, b = map(int, input().split())
        if (a == 0 and b == 0):
            break
        else:
            print(a+b)

def step_10951():
    while True:
        try:
            a, b = map(int, input().split())
            print(a+b)
        except:
            break

def step_1110():
    n = int(input())
    num = n
    cycle = 0

    while True:
        a = num // 10
        b = num % 10
        c = (a+b) % 10
        num = (b*10) + c

        cycle = cycle + 1
        if(num == n):
            break
    print(cycle)
            

if __name__ == '__main__':
   step_1110()