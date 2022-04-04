# your code 부분에 코딩하여 문제를 풀이해주세요.
# print 함수가 포함되어 있으면 주차 점수 0점 처리하겠습니다. 4주차 과제에는 출력을 요구하는 문제가 없습니다.
# input 함수가 포함되어 있으면 주차 점수 0점 처리하겠습니다. 4주차 과제에는 입력을 요구하는 문제가 없습니다.
# answer 변수를 사용하여 문제를 풀이하세요. 반환값은 answer 변수입니다.
# 함수 내에서 컴파일 에러, 런타임 에러가 발생하면 해당 문제 점수 0점 처리하겠습니다.
# 함수명 변경하지 마세요. 변경 시 해당 문제 점수 0점 처리하겠습니다.
# 제출 기한: 2022년 4월 5일 23시 59분.
# 지각 제출 기한: 2022년 4월 6일 23시 59분. 주차 점수에서 20% 감점

# 문제 1번
def intervention(queue):
    answer = list()
    exist = queue.count("성은")
    if exist == 0:
        queue.append("승호")
    elif exist == 1:
        position = queue.index("성은")
        if position > 3:
            queue.insert(position + 1, "승호")
        else:
            queue.append("승호")
    answer = queue
    return answer

# 문제 2번
def pascal(n):
    answer = list()
    pasc = [1]
    new_list = []
    for i in range(1, n):
        pasc = [0] + pasc + [0]
        for j in range(1, i+2):
            new_list.append(pasc[j-1] + pasc[j])
        pasc = new_list
        new_list = []
    answer = pasc
    return answer

# 문제 3번
def auto_complete(entry, searchWords):
    answer = list()
    classify = []
    for i in range(0, len(searchWords)):
        if entry in searchWords[i]:
            classify.append(searchWords[i])
    classify.sort()
    answer = classify
    return answer



# 문제 4번
def stock_price(stockChart):
    answer = str()
    sum = 0
    price = []
    gap = []
    for i in range(len(stockChart)):
        sum = sum+ int(stockChart[i])
        price.append(sum)
    for j in range(len(price)):
        gap.append(int(price[j]) - int(len(price)-1))
    s = min(gap)
    gap.reverse()
    date = gap.index(s)
    if date == 0:
        answer = "아니야 조금만 더 기다려"
    else:
        answer = "%s일 전에 샀어야지 으이구"%date
    return answer

# 문제 5번
def decryption(letter):
    answer = str()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    decoding = "xyzabcdefghijklmnopqrstuvw"
    no_chr = 0
    for i in letter:
        for j in alphabet:
            if i != j:
                no_chr = no_chr + 1        
            elif i == j:
                answer = answer + decoding[alphabet.index(j)]
        if no_chr == len(alphabet):
            answer = answer + i
            no_chr = 0
        else:
            no_chr = 0
    return answer