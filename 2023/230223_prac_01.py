def step_24313():
    a1, a2 = map(int, input().split())
    c = int(input())
    nn = int(input())
    if (a1*nn+a2 <= c*nn) and (c-a1 >=0):
        print("1")
    else:
        print("0")


if __name__ == '__main__':
    step_24313()