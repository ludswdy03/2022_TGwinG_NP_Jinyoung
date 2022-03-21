# 문제 1번
def sum(a,b):
    x = a + b
    return x

# 문제 2번
def sub(a,b):
    y = a - b
    return y

# 문제 3번
def mul(a,b):
    m = a * b
    return m

# 문제 4번
def div(a,b):
    n = a / b
    return n

# 문제 5번
def distance(x1,y1,x2,y2):
    d = pow((((x1 - x2) ** 2) + ((y1 - y2) ** 2)), 1/2)
    return d

# 문제 6번
def short():
    lylic = "life is short art is long"
    srt = lylic[8:13]
    return srt

# 문제 7번
def myReverse(string):
    r = string[::-1]
    return r

# 문제 8번
def letMeIntroduceMyself():
    name = input("이름을 입력하시오: ")
    hobby = input("취미를 입력하시오: ")
    univ = input("재학 중인 대학을 입력하시오: ")
    birth = input("생일을 입력하시오(예시: 031024): ")
    intro = "제 이름은 %s입니다. 제 취미는 %s이구요. 저는 %s를 다니고 있습니다. 제 생일은 %s월 %s일 입니다." %(name, hobby, univ, birth[2:4], birth[4:])
    print(intro)
    return intro

# 문제 9번
def calcAI():
    num_1 = int(input("첫 번째 숫자를 입력하시오: "))
    num_2 = int(input("두 번째 숫자를 입력하시오: "))
    cal = "두 수의 합은 %d 입니다." %(num_1 + num_2)
    print(cal)
    return cal
