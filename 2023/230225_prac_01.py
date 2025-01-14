def hanoi(n, start, end):
    if n == 1:
        print("start end === ", start, end)
        return
    hanoi(n-1, start, 6-start-end) 
    print(start,end)
    hanoi(n-1, 6-start-end, end)

def step_11729():
    n = int(input())
    print(2**n-1)
    hanoi(n, 1, 3)


if __name__ == '__main__':
    step_11729()