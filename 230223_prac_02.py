def facto_1(n):
    if(n>1):
        return n * facto_1(n-1)
    else:
        return 1

def step_10872():
    a = int(input())
    print(facto_1(a))

def facto_2(n):
    if n<=1:
        return n
    return facto_2(n-1) + facto_2(n-2)

def step_10870():
    a = int(input())
    print(facto_2(a))

if __name__ == '__main__':
    step_10870()