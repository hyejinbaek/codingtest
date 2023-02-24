import sys
input = sys.stdin.readline

def isPalindrome(r, l):
    global count, s
    count += 1
    if r >= l: 
        return 1
    elif s[r] != s[l]: 
        return 0
    return isPalindrome(r + 1, l - 1)
    

def step_25501():
    global count, s
    for _ in range(int(input())):
        count = 0
        s = input()
        print(isPalindrome(0, len(s) - 2), count)

def merge_sort(A, p, r):
    if(p < r and count <=K):
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)
        
def merge(A, p, q, r):
    global count, result
    i = p
    j = q+1
    tmp = []
    
    while i <= q and j <= r:
        if(A[i] <= A[j]):
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1
        
    while i <= q:
        tmp.append(A[i])
        i += 1
    
    while j <= r:
        tmp.append(A[j])
        j += 1
    
    i, t = p, 0
    
    while i <= r:
        A[i] = tmp[t]
        count += 1
        if count == K:
            result = A[i]
            break
        i += 1
        t += 1

def step_24060():
    global count, K, result, s
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    count = 0
    result = -1
    merge_sort(A, 0, N - 1)
    print(result)

def star(n):
    if n == 1:
        return ['*']
    stars = star(n//3)
    print("stars === ", stars)
    l = []

    for s in stars:
        l.append(s*3)
    for s in stars:
        l.append(s+' '*(n//3)+s)
    for s in stars:
        l.append(s*3)
    return l

def step_2447():
    n = int(input())
    print('\n'.join(star(n)))


if __name__ == '__main__':
    step_2447()