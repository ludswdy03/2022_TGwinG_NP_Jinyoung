# 이번 주차부터는 컴파일 에러 등으로 프로그램 자체가 실행되지 않을 시에는 과제 점수 0점 처리합니다.
# 문제에서 요구하는 입출력 외에는 절대 포함해서 제출하지 마세요. 0점 처리합니다.
# 문제에서 요구하는 출력 형식, 반환 형식을 "모두" 지켜주세요. 지키지 않으면 오답처리 됩니다.
# 한 파일에 모든 문제를 풀이해서 제출하세요. 분리 제출 시 채점자 PC기준 최상위에 정렬되는 파일만 채점합니다.
# 제출 마감일: 2022-03-29 23:59, 지각 제출 시 점수에서 20% 감점입니다.

# 문제 1번
def question1():
    return "next"

# 문제 2번
def leapYear(year):
    if year % 4 == 0 and year % 100 != 0:
        month = "윤년입니다."
    elif year % 400 == 0:
        month = "윤년입니다."
    else:
        month = "윤년이 아닙니다."
    return month

# 문제 3번
def alram(time):
    if 0 <= time < 44:
        c_time = 2315 + time
    else:
        hour = time // 100
        minute = time % 100
        time_2_min = (hour * 60) + minute
        minus_45 = time_2_min - 45
        m_hour = minus_45 // 60
        m_min = minus_45 % 60
        c_time = (m_hour * 100) + m_min
    
    if 0 <= c_time <= 59:
        c_time = str(c_time)
        alarm = "오전 0시 %s분" %c_time
    elif 100 <= c_time <= 959:
        c_time = str(c_time)
        alarm = "오전 %s시 %s분" %(c_time[:1], c_time[1:])
    elif 1000 <= c_time <= 1159:
        c_time = str(c_time)
        alarm = "오전 %s시 %s분" %(c_time[:2], c_time[2:])
    elif 1200 <= c_time <= 2359:
        c_time = str(c_time)
        alarm = "오후 %s시 %s분" %(c_time[:2], c_time[2:])
    return alarm

# 문제 4번
def findDaesun(x1,y1,r1,x2,y2,r2):
    d = pow(pow(x1 - x2, 2) + pow(y1 - y2, 2), 1/2)
    if d == 0 and r1 == r2:
        num_coor = "어딘지 모르겠다 오바"
    elif abs(r1- r2) < d < r1 + r2:
        num_coor = 2
    elif d == r1 + r2 or d == abs(r1 - r2):
        num_coor = 1
    elif d > r1 + r2 or d < abs(r1 - r2):
        num_coor = 0
    return num_coor