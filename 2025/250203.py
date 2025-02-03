# 팰린드롬인지 확인하기 (10988번)

n = input()


if n[::1] == n[::-1]:
    print(1)
else:
    print(0)