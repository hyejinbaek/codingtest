def step_1712():
    a, b, c = map(int, input().split())
    if b>=c:
        print(-1)
    else:
        print(int(a/(c-b)+1))

def step_2292():
    n = int(input())
    num = 1
    cnt = 1
    while n > num:
        num += 6 * cnt
        cnt += 1
    print(cnt)

def step_1193():
    x = int(input())
    line=1
    while x>line:
        x -= line
        line += 1
    if line % 2 == 0:
        a = x
        b = line-x+1
    else:
        a = line-x+1
        b = x
    print(a, '/', b, sep='')
    
def step_2869():
    a, b, v = map(int, input().split())
    day = (v - b) / (a - b)
    print(int(day) if day == int(day) else int(day)+1)
            

if __name__ == '__main__':
    step_2869()