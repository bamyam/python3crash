hanbitMenus = {'쌀 ': 9900, '상추': 1900, '고추': 2900, '마늘': 8900, '통닭': 5600, '햄 ': 6900, '치즈': 3900}

def readSale():
    print('---------------------------------------')
    print('-- 한빛마트 오늘의 할인 가격표 출력 시스템 --')
    print('---------------------------------------')
    sale = int(input('오늘의 할인율을 입력하세요.'))
    return sale

def convertSale(sale):
    prices = []
    for val in hanbitMenus.values():
        price = val * (1 - (sale / 100))
        prices.append(price)
    return prices

def printSaledPrice(sale, prices):
    for idx, menu in enumerate(hanbitMenus.keys()):
        print(f'{menu:4s} : {hanbitMenus[menu]:,d} 원 {sale} %DC -> {prices[idx]:,.0f} 원')

sale = readSale()
prices = convertSale(sale)
printSaledPrice(sale, prices)

# sale, prices = convertSale()
# for idx, menu in enumerate(hanbitMenus.keys()):
#     print(f'{menu:3} : {hanbitMenus[menu]:,d} 원 {sale} %DC -> {prices[idx]:,.0f} 원')

def readTaxInfor():
    isMarried = input('결혼여부는? (1 : 미혼, 2 : 기혼')
    sal = int(input('연봉은? '))
    return isMarried, sal

#처리
def taxCalculation(isMarried, sal):
    if isMarried == '1':
        if sal >= 3000 : tax = sal * 0.25
        else: tax = sal * 0.1
    else:
        if sal >= 6000: tax = sal * 0.35
        else: tax = sal * 0.15
    return tax

#출력

def printTax(isMarried, sal, tax):
    return print(f'{isMarried} {sal} {tax}')

isMarried, sal = readTaxInfor()
tax = taxCalculation(isMarried, sal)
printTax(isMarried, sal, tax)

# 한글 출력시 간격 일정하게 맞추기
from hangleUtil import preFormat

def printSaledPrice2(sale, prices):
    for idx, menu in enumerate(hanbitMenus.keys()):
        print(f'{preFormat(menu, 5)} : {preFormat(str(hanbitMenus[menu]), 7)} 원 '
              f'{preFormat(str(sale), 3)} %DC -> {preFormat(str(prices[idx]), 7)} 원')

printSaledPrice2(sale, prices)

# 변수의 유효범위 : scope
# 지역변수 : 블럭내에 선언한 변수, 특정 블럭내에서만 유효
# 전역변수 : 소스내에 선언한 변수, 모든 범위에서 유효
# 함수 내에서 선언한 변수는 함수 밖에서 접근 가능?
# => 함수내에서 선언한 변수는 함수내에서만 사용가능

num1 = 10 # 전역변수
print(num1)
def func1():
    global num3  # global 지역변수로 선언
    num2 = 100   # 지역변수
    num3 = 999
    print(num1)  # 함수 내에서 전역변수 출력
    print(num2)  # 함수 내에서 지역변수 출력
    print(num3)

func1()
print(num2)      # func1 함수 내에 선언된 지역변수 출력  (오류발생)
print(num3)      # func1 함수 내에 선언된 global 지역변수 출력 (정상출력)

# 만일, 함수내에서 전역변수의 값을 수정하고 싶다면?
# => global 문 사용 (비추!)
# => 매개변수, return문 사용 (추천!)

num1 = 99
num2 = 'abc'
def func2():
    global num2     # 전역변수를 함수 내에서 수정하기 위해서 global로 선언
    num1 = 77
    num2 = 'xyz'    # 전역변수를 함수 내에서 수정
    print(num1)
    print(num2)

func2()
print(num1)
print(num2)         # 함수 내에서 수정한 값이 함수 밖에서도 유지됨

num3 = 33

def func3(num3):
    print('func3: ', num3)
    num3 = 44
    print('func3: ', num3)

print(num3)
func3(num3)
print(num3)

# (call by value) vs (call by reference)
# 파이썬에서는 기본자료형(숫자, 논리) 변수를 함수의 매개변수로 넘기는 경우
# call by value(값에 의한 호출)가 발생하며 이것은 다른 메모리에 값을 복사해서 넣기 때문에
# 함수내 매개변수와 호출 시 전달한 변수는 서로 다른 것으로 인식됨!

# 반면, 참조자료형 변수(문자형, 컨테이너형)를 함수의 매개변수로 넘기는 경우
# call by reference(주소에 의한 호출)가 발생하며, 같은 메모리의 값을 복사하기 때문에
# 함수내 매개변수와 호출시 전달한 변수는 서로 동일한 것으로 인식됨!

# 단 파이썬은 call by value/reference라기 보다
# passed by assignment(어떤 값을 전달하느냐에 따라)로 다뤄지고 있음

# 웹사이트 방문횟수 조회 프로그램
# global로 선언하면 숫자형이든 문자형이든 입력이 됨
# 선언 안하면 문자형도 전역변수에 적용이 안 됨
visit = '0'
def website(visit):
    while True :
        menu = input('1. 웹사이트 방문, 2. 종료')
        visit = int(visit)
        if menu == '1':
            visit += 1
        else :
            break
    return visit

website(visit)
print(visit)

visit2 = 0
def website2():
    global visit2
    while True :
        menu = input('1. 웹사이트 방문, 2. 종료')
        if menu == '1':
            visit2 += 1
        else :
            break
    return visit2

website2()
print('누적방문 횟수', visit2)

# 웹사이트 방문횟수 조회 프로그램
visits = 0 # 방문횟수

# while True :
#     job = input('작업은? (1. 웹사이트 방문, 2. 종료)')
#     if job == '1':
#         visits += 1
#         print('누적 방문 횟수', visits)
#     elif job == '2':
#         break

def visitTime():
    #visits = 0   # 지역변수
    global visits # 전역변수
    while True :
        job = input('작업은? (1. 웹사이트 방문, 2. 종료)')
        if job == '1':
            visits += 1
            print('누적 방문 횟수', visits)
        elif job == '2':
            break

visitTime()
print(visits)

# 주민번호를 입력받아 유효성을 검사하는
# checkJumin 함수를 작성하세요
# 1. 주민번호 맨 끝자리를 제외한 나머지 번호들의
#    각자리를 2,3,4,5,6,7,8,9,2,3,4,5 가중치로 곱합
# 2. 곱한 결과를 각각 모두 더함
# 3. 더한 값을 11로 나눠 구한 나머지를 11에서 뺌
# 4. 이렇게 구한 결과와 주민번호 맨 마지막 자리의 일치여부 검사
# 5. 만약, 구한 결과가 2자리라면 맨 끝자리와 비교함
#     맨 끝자리는 일의 자리로 10으로 나눴을 때 나머지로 구하면 됨

def juminInfo():
    juminNum = input('주민번호를 입력하세요')
    gop = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 0]
    hap = 0
    return juminNum, gop, hap

def computeJumin(juminNum, gop, hap):
    for idx, num in enumerate(juminNum):
        hap += int(num) * gop[idx]
    ilchi = 11 - (hap % 11)
    return ilchi
def juminNum():
    juminNum, gop, hap = juminInfo()
    ilchi = computeJumin(juminNum, gop, hap)
    if len(str(ilchi)) == 2:
        print(f'{ilchi} 와 {juminNum[-2:]}')
    else:
        print(f'{ilchi} 와 {juminNum[-1]}')

juminNum()

# 선생님 버전
jumin = input('주민번호는?')
#jumin = '111111-1111118'
sum = 0

sum += int(jumin[0]) * 2
sum += int(jumin[1]) * 3
sum += int(jumin[2]) * 4
sum += int(jumin[3]) * 5
sum += int(jumin[4]) * 6
sum += int(jumin[5]) * 7
sum += int(jumin[7]) * 8
sum += int(jumin[8]) * 9
sum += int(jumin[9]) * 2
sum += int(jumin[10]) * 3
sum += int(jumin[11]) * 4
sum += int(jumin[12]) * 5


checker = 11 - sum % 11
print(checker)

if checker == int(jumin[13]):
    print('주민번호 유효')
else :
    print('주민번호 불일치')

def checkJumin():
    jumin = input('주민번호는?')
    pos = [0, 1, 2, 3 ,4, 5, 7, 8, 9, 10, 11, 12]
    weight = [2, 3 ,4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
    sum = 0
    result = '주민버호 불일치'
    for i in range(len(pos)):
        sum += int(jumin[ pos[i] ]) * weight[i]

    checker = (11 - (sum % 11)) % 10
    if checker == int(jumin[13]):result = '주민번호 유효!'
    print(result)

checkJumin()





