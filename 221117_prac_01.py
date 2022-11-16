# (p. 115) 예제 4-3 왕실의 나이트
'''

8 x 8 좌표 평면
이동은 L자형태로 가능
1. 수평으로 두칸 이동한 뒤 수직으로 한칸 이동(c2)
2. 수직으로 두칸 이동한 뒤 수평으로 한칸 이동(b3)
행 위치는 1~8로, 열 위치는 a~h로 표현
'''


input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0]))-int(ord('a'))+1
print(column)
steps = [(-2,-1), (-1,-2), (1, -2), (2,-1), (2,1), (1,2),(-1, 2), (-2, 1)]
result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)