# 백준 1. 입출력과 사칙연산
def step_18108():
    year = int(input())
    print(year - 543)


def step_3003():
    chess = [1,1,2,2,2,8]
    a = list(map(int, input().split()))
    for i in range(6):
        print(chess[i]-a[i], end=' ')

def step_10430():
    a, b, c = map(int, input().split())
    print((a+b)%c, ((a%b) + (b%c))%c, (a*b)%c, ((a%c)*(b%c))%c, sep = '\n') 

def step_2588():
    A = int(input())
    B = input()

    AxB2 = A * int(B[2])
    AxB1 = A * int(B[1])
    AxB0 = A * int(B[0])
    AxB = A * int(B)

    print(AxB2, AxB1, AxB0, AxB, sep='\n')

def step_10171():
    # 역슬래시(\)는 두개 사용
    print("\\    /\\")
    print(" )  ( ')")
    print("(  /  )")
    print(" \\(__)|")

def step_10172():
    print("|\\_/|")
    print("|q p|   /}")
    print('( 0 )"""\\')  # \'앞에 \을 붙여준다.
    print('|"^"`    |')
    print("||_/=\\\__|")

def step_25083():
    print('         ,r\'"7')
    print("r`-_   ,'  ,/ ")
    print(" \\. \". L_r'")
    print("   `~\\/")
    print("      |")
    print("      |")

if __name__ == '__main__':
   step_25083()