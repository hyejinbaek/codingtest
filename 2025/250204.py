# 너의 평점은 (25206번)


raw_data = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 
        'B0': 3.0, 'C+': 2.5, 'C0': 2.0,
        'D+': 1.5, 'D0': 1.0, 'F':0.0}
sum = 0
sum_g = 0

for i in range(20):
    subject, grade, point = input().split()
    if point =='P':
        continue
    else:
        sum += float(grade)*raw_data[point]
        sum_g += float(grade)
print(sum/sum_g)