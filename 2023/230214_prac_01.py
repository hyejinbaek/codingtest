def step_1978():
    n = int(input())
    num = list(map(int, input().split()))
    s = 0
    for i in num:
        cnt = 0
        if i==1:
            continue
        for j in range(2, i+1):
            if i % j ==0:
                cnt += 1
        if cnt == 1:
            s += 1
    print(s)

def step_2581():
    m = int(input())
    n = int(input())
    a = []
    for num in range(m, n+1):
        error = 0
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    error += 1
                    break
            if error == 0:
                a.append(num)
    if len(a)>0:
        print(sum(a))
        print(min(a))
    else:
        print(-1)

def step_11653():
    n = int(input())
    m = 2
    while n != 1:
        if n % m == 0:
            print(m)
            n = n//m
        else:
            m+=1

def step_1929():
    m,n = map(int, input().split())
    for i in range(m, n+1):
        if i == 1:
            continue
        for j in range(2, int(i**0.5)+1):
            if i%j == 0:
                break
        else:
            print(i)

def step_4948():
    import math
    m = 123456

    arr1 = [True for _ in range(2*m+1)]
    arr1[0], arr1[1] = False, False

    for i in range(2, int(math.sqrt(2*m)+1)):
        if arr1[i]:
            j = 2
            while i * j <= 2*m:
                arr1[i*j] = False
                j+=1
    while True:
        n = int(input())
        if n == 0:
            break
        count = 0
        for i in range(n+1, 2*n+1):
            if arr1[i]:
                count += 1
        print(count)

def step_9020():
    arr = [0 for i in range(10001)]
    arr[1]=1
    for i in range(2, 98):
        for j in range(i*2, 10001, i):
            arr[j] = 1
    t = int(input())
    for i in range(t):
        a = int(input())
        b = a//2
        for j in range(b, 1, -1):
            if arr[a-j] == 0 and arr[j]==0:
                print(j, a-j)
                break

if __name__ == '__main__':
    step_9020()