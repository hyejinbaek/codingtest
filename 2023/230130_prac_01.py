def step_11654():
    alpha = input()
    print(ord(alpha))

def step_11720():
    n = input()
    print(sum(map(int, input())))

def step_10809():
    s = input()
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for i in alpha:
        if i in s:
            print(s.find(i), end = ' ')
        else:
            print(-1, end= ' ')

def step_2675():
    t = int(input())
    for i in range(t):
        n, s = input().split()
        txt = ''
        for i in s:
            txt += int(n) * i
        print(txt)

def step_1157():
    alpha = input().upper()
    alpha_list = list(set(alpha))
    cnt = []
    for i in alpha_list:
        count = alpha.count
        cnt.append(count(i))
    if cnt.count(max(cnt))>1:
        print("?")
    else:
        print(alpha_list[(cnt.index(max(cnt)))])


if __name__ == '__main__':
    step_1157()