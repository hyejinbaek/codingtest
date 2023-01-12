def step_1330():
    a, b = map(int, input().split())
    if a > b:
        print(">")
    elif a < b:
        print("<")
    else:
        print("==")

def step_9498():
    score = int(input())
    if 90<=score<=100:
        print("A")
    elif 80<=score<=89:
        print("B")
    elif 70<=score<=79:
        print("C")
    elif 60<=score<=69:
        print("D")
    else:
        print("F")

def step_2753():
    year = int(input())
    if ((year%4 == 0)and(year%100 != 0)) or (year%400 == 0):
        print("1")
    else:
        print("0")

def step_14681():
    x = int(input())
    y = int(input())
    if 0<x<=1000 and 0<y<=1000:
        print("1")
    elif -1000<=x<0 and 0<y<=1000:
        print("2")
    elif -1000<=x<0 and -1000<=y<0:
        print("3")
    else:
        print("4")

def step_2884():
    h, m = map(int, input().split())
    if m>44:
        print(h, m-45)
    elif m < 45 and h > 0:
        print(h-1, m+15)
    else:
        print(23, m+15)

def step_2525():
    A, B = map(int, input().split())
    C = int(input())

    hour = (B+C)//60
    min = (B+C)%60

    if(B + C >= 60):
        if(A+hour >= 24):
            A = A - 24
        A = A + hour
        print(A, min)
    else:
        if(A >= 24):
            A = A - 24
        print(A, B+C)

def step_2480():
    a, b, c = map(int, input().split())
    if a==b==c:
        print(10000+a*1000)
    elif a==b or b==c:
        print(1000+b*100)
    elif a==c:
        print(1000+a*100)
    else:
        print(100 * max(a,b,c))

if __name__ == '__main__':
   step_2480()