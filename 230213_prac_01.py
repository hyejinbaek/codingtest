def step_10250():
    t = int(input())
    for i in range(t):
        # h : 호텔의 층 수, w : 각 층의 방 수, n : 몇 번째 손님
        h, w, n = map(int, input().split())
        num = n//h + 1
        floor = n % h
        if n % h == 0:  # h의 배수이면,
            num = n//h
            floor = h
        print(f'{floor*100+num}')

def step_2775():
    t = int(input())
    for i in range(t):
        k = int(input())
        n = int(input())
        p = [i for i in range(1, n+1)]

        for x in range(k):
            for y in range(1, n):
                p[y] += p[y-1]
        print(p[-1])

def step_2839():
    n = int(input())

    if n % 5 == 0:
        print(n//5)
    else:
        p = 0
        while n > 0:
            n -= 3
            p += 1
            if n % 5 == 0:
                p += n // 5
                print(p)
                break
            elif n == 1 or n == 2:
                print(-1)
                break
            elif n == 0:
                print(p)
                break

def step_10757():
    a,b = map(int, input().split())
    print(a+b)


if __name__ == '__main__':
    step_10757()