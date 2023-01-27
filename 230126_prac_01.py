def step_4673():
    numbers = set(range(1, 10000))
    remove_set = set()  # 생성자가 있는 숫자 set
    for num in numbers:
        for n in str(num):
            num += int(n)
        remove_set.add(num)  # add: 집합에 요소를 추가할 때

    self_numbers = numbers - remove_set  # set의 '-' 연산자로 차집합을 구함
    for self_num in sorted(self_numbers):  # sorted 함수로 정렬
        print(self_num)

def step_1065():
    n = int(input())
    h = 0
    for i in range(1, n+1):
        num_list = list(map(int, str(i)))
        if i < 100:
            h += 1
        elif num_list[0] - num_list[1] == num_list[1] - num_list[2]:
            h += 1
    print(h)

if __name__ == '__main__':
    step_1065()