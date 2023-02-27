def step_2798():
    n, m = map(int, input().split())
    card = list(map(int, input().split()))
    res = 0
    for i in range(n):
        for j in range(i+1, n):
            for z in range(j+1, n):
                card_total = card[i]+card[j]+card[z]
                if card_total <= m:
                    res = max(res, card_total)
    print(res)

def step_2231():
    n = int(input())
    for i in range(1, n+1):
        num = sum((map(int, str(i))))
        num_s = i + num
        if num_s == n:
            print(i)
            break
        if i == n:
            print(0)

def step_7568():
    n = int(input())
    lst = []
    for i in range(n):
        w, h = map(int, input().split())
        lst.append((w, h))
        print("lst ===", lst)
    for i in lst:
        rank = 1
        for j in lst:
            if i[0] < j[0] and i[1]<j[1]:
                rank += 1
        print(rank, end = " ")
    
        

if __name__ == '__main__':
    step_7568()