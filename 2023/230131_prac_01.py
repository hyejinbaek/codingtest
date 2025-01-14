def step_1152():
    txt = input().split()
    print(len(txt))

def step_2908():
    a, b = input().split()
    a = int(a[::-1])
    b = int(b[::-1])

    if a > b:
        print(a)
    else:
        print(b)

def step_5622():
    alpha = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
    dial = input()

    time = 0
    for unit in alpha:
        for i in unit:
            for x in dial:
                if i == x:
                    time += alpha.index(unit) + 3
    print(time)

def step_2941():
    alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
    txt = input()

    for unit in alpha:
        txt = txt.replace(unit, '*')
    print(len(txt))

def step_1316():
    n = int(input())
    group = 0
    for _ in range(n):
        word = input()
        error = 0
        for index in range(len(word)-1):
            if word[index] != word[index+1]:
                new_word = word[index+1:]
                if new_word.count(word[index]) > 0:
                    error += 1
        if error == 0:
            group += 1
    print(group)

if __name__ == '__main__':
    step_1316()