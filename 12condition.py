# if 문
# 특정 조건을 만족하면 지정한 문장을 실행하는 조건문
# if 조건식 :
#   수행할 문장(들)

# 속도위반 체크 프로그램
# 기준속도 : 50 km/h

speed = int(input('현재 속도 :'))
if speed > 50:
    print(f'현재 속도는 {speed}으로, 과속입니다')

# 파이썬의 코드 블록
# 특정한 동작을 위한 코드를 한 곳에 모아둔 것
# 이러한 코드들은 반드시 같은 들여쓰기 내에 있어야 함

# 조건식이 True일 경우 무조건 코드블록을 실행함
if True:
    print('Hello World!!')

# if ~ else 문
# if문은 조건이 참일때만 지정한 코드를 실행하는데 비해
# if ~ else문은 조건이 참일 때와 거짓일 때 각각 지정한 코드를 실행함

mecTemp = int(input('기계 온도 :'))

if mecTemp >= 40 :
    print('팬(Fan) 가동')
else :
    print('팬(Fan) 중지')

number = int(input('양의 정수 입력 :'))
result = number / 3
print(result)

if (result-int(result)) >= 0.5:
    result = int(result) + 1
else:
    result = int(result)

print(number, '결과 :', result)

# 중첩 if문
# if문 속에 또 다른 if문을 포함시켜 작성하는 조건문
# 조건문을 중첩할때는 들여쓰기에 유의해야 함
# 다양한 조건에 따라 결과를 처리하고 싶을때 사용

# 평균이 73.5라 할때 조건에 따라
# 수/우/미/양/가 학점을
# 출력하는 조건문을 작성하세요

avg = 73.5

if avg >= 90: print('수')
else:
    if avg >= 80: print('우')
    else:
        if avg >= 70: print('미')
        else:
            if avg >= 60: print('양')
            else:
                print('가')

# 다중if문
# 중첩 if문을 작성하는 경우 조건이 많으면 다소 복잡함
# 이러한 중첩 문을 단순하게 처형할 수 있는 조건문
#if 조건식1:
#    실행할 문장
# elif 조건식2:
#     실행할 문장
# elif 조건식3 :
#     실행할 문장

if avg >= 90:
    print('수')
elif avg >= 80 : print('우')
elif avg >= 70 : print('미')
elif avg >= 60 : print('양')
else : print('가')

# 자동 주문 시스템
# 다국어를 지원하기 위해 사용자가 원하는 언어에 따라 주문을 받는 시스템
#기본은 영어

infor = int(input('''
Good morning. Nice to meet you.
Where are you from?
Please select a number
1. 대한민국  2. USA  3. 中国
'''))
if infor == 1:
    print('주문하시겠어요?')
elif infor == 2:
    print('Would you like to order?')
elif infor == 3 :
    print('您要点菜吗？')
else :
    print('Would you like to order?')

# bmi 지수에 따른 결과 출력
weight = int(input('몸무게 입력 :'))
height = int(input('키 입력 :'))
bmi = weight / (height / 100) ** 2

if bmi > 35: result = '초고도비만'
elif bmi >= 30: result = '고도비만'
elif bmi >= 25: result = '비만'
elif bmi >= 23: result = '과체증'
elif bmi >= 18.5:result = '정상제충'
else : result = '저체중'

print(f'{weight}, {height}, {bmi:.1f}, {result}')
print(f'')

x = (26.7 * (171/100) ** 2) - (25 * (171/100) ** 2)
print(x)

# 누진세 적용 전기요금 계산
# 입력
useElec = float(input('전기사용량 :'))
default = None
price = None
pay = None

# 처리
if useElec > 400 :
    default = 7300
    price = 280.6
    pay = (useElec * price) + default
elif useElec > 200 and useElec <= 400 :
    default = 1600
    price = 187.9
    pay = (useElec * price) + default
else :
    default = 910
    price = 99.3
    pay = (useElec * price) + default

#출력
print(f'''
사용량 : {useElec} kwh
기본요금 : {default} 원
단가 : {price} 원
전기 요금 : {pay} 원
''')

# 윤년여부 계산
# 입력
for _ in range(5) :
    year = int(input('현재년도 :'))
    # 처리
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(f'{year}년은 윤년입니다')
    else :
        print(f'{year}년은 윤년이 아닙니다')

