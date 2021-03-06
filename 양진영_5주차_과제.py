# your code 부분에 코딩하여 문제를 풀이해주세요.
# print 함수가 포함되어 있으면 주차 점수 0점 처리하겠습니다. 5주차 과제에는 출력을 요구하는 문제가 없습니다.
# input 함수가 포함되어 있으면 주차 점수 0점 처리하겠습니다. 5주차 과제에는 입력을 요구하는 문제가 없습니다.
# result 변수를 사용하여 문제를 풀이하세요. 반환값은 result 변수입니다.
# 함수 내에서 컴파일 에러, 런타임 에러가 발생하면 해당 문제 점수 0점 처리하겠습니다.
# 함수명 변경하지 마세요. 변경 시 해당 문제 점수 0점 처리하겠습니다.
# 제출 기한: 2022년 4월 12일 23시 59분.
# 지각 제출 기한: 2022년 4월 13일 23시 59분. 주차 점수에서 20% 감점

def calcCircleArea(r):
    result = float()
    r = float(r)
    from math import pi
    s  = pow(r, 2) * pi
    result = round(s, 2)
    return result
def calcLog(a, b):
    result = float()
    from math import log, e
    if a == "e":
        a = e
        if b == "e":
            b = e
        else:
            b = float(b)
    elif b == "e":
        b = e
        if a == "e":
            a = e
        else:
            a = float(a)
    else:
        a, b = float(a), float(b)
    l = log(a, b)
    result = round(l, 2)
    return result
def calcSin(x):
    result = float()
    x = float(x)
    from math import sin
    s = sin(x)
    result = round(s, 2)
    return result
def calcFactorial(x):
    result = int()
    x = int(x)
    from math import factorial
    result = factorial(x)
    return result
def calcCombination(n, r):
    result = int()
    n, r = int(n), int(r)
    from math import factorial
    result = int(factorial(n) / factorial(n - r) / factorial(r))
    return result

def calculator(order):
    answer = 0
    v1 = order.split()[-1]
    v2 = order.split()[-2]
    if "원넓이:" in order:
        answer = calcCircleArea(v1)
    elif "로그:" in order:
        answer = calcLog(v1, v2)
    elif "사인:" in order:
        answer = calcSin(v1)
    elif "팩토리얼:" in order:
        answer = calcFactorial(v1)
    elif "조합:" in order:
        answer = calcCombination(v2, v1)
    return answer