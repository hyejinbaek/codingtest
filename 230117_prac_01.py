def step_10807():
    n = int(input())
    a = list(map(int, input().split()))
    v = int(input())
    print(a.count(v))

def step_10871():
    n,x = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(n):
        if a[i] < x:
            print(a[i], end = ' ')

def step_10818():
    n = int(input())
    n_list = list(map(int, input().split()))
    print(min(n_list), max(n_list))

def step_2562():
    num = []
    for _ in range(9):
        n = int(input())
        num.append(n)
    print(max(num))
    print(num.index(max(num))+1)

def step_5597():
    total = [i for i in range(1,31)]
    for _ in range(28):
        n = int(input())
        total.remove(n)
    print(min(total))
    print(max(total))

def step_3052():
    a = []
    for i in range(10):
        n = int(input())
        a.append(n%42)
    a = set(a)
    print(len(a))

def step_1546():
    n = int(input())
    test = list(map(int, input().split()))
    max_test = max(test)

    grade = []
    for i in test:
        grade.append(i/max_test*100)
    test_avg = sum(grade)/n
    print(test_avg)

def step_8958():
    testcase = int(input())
    for _ in range(testcase):
        n = list(input())
        score = 0
        sum_score = 0
        for ox in n:
            if ox =='O':
                score += 1
                sum_score += score
            else:
                score=0
        print(sum_score)

def step_4344():
    c = int(input())
    for _ in range(c):
        num = list(map(int, input().split()))
        avg = sum(num[1:])/num[0]
        cnt = 0
        for score in num[1:]:
            if score > avg:
                cnt += 1
        rate = cnt/num[0] * 100
        print(f'{rate:.3f}%')


if __name__ == '__main__':
   step_4344()