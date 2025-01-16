# 백준
# 바구니 뒤집기(10811번)

def reverse_baskets():
    n, m = map(int, input().split())
    
    basket = list(range(1, n+1))
    
    for _ in range(m):
        i, j = map(int, input().split())
        basket[i-1:j] = reversed(basket[i-1:j])
        
    print(*basket)
    
if __name__ == "__main__":
    reverse_baskets()
