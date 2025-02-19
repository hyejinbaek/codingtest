# 숫자 카드 (10815번)

n = int(input())
# set으로 변환하여 시간 단축
n_num = set(map(int, input().split()))

m = int(input())
m_num = list(map(int, input().split()))

total = [1 if num in n_num else 0 for num in m_num]
print(' '.join(map(str, total)))

