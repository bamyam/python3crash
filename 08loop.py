# 반복문
# 특정 문장/코드를 지정한 횟수/조건에 의해 반복 실행하는 문장

# 간단한 메시지를 출력
print('너무 추운 날씨입니다')

# 메세지를 여러번 출력
print('너무 추운 날씨입니다')
print('너무 추운 날씨입니다')
print('너무 추운 날씨입니다')

# 메세지를 수정할 필요가 생긴다면? - 수정 불편!
print('너무 추운 날씨입니다, 따뜻하게 입으세요')
print('너무 추운 날씨입니다, 따뜻하게 입으세요')
print('너무 추운 날씨입니다, 따뜻하게 입으세요')

# 만약, 반복문을 사용한다면?
# 반복과 수정이 용이해짐

# 파이썬의 반복문
# for : 지정한 횟수만큼 반복 수행
# while : 지정한 조건에 의해 반복 수행
# for문
# for 변수 in range(시작값, 종료값, 증가/감소):
#   반복할 문장
# 반복횟수는 range(시작값, 종료값)로 유추가능
# 즉, 횟수는 종료값 - 시작값 - 1로 계산됨
# range 함수는 시작값과 종료값 - 1 사이의 연속된 정수들을 반환하는 함수

list(range(1,10+1))
list(range(1, 3, 1))

# iterable 객체
# 값을 차례대로 꺼내 볼 수 있는 객체를 의미함
# 보통 리스트, 튜플, 딕셔너리 등의 객체를 의미
# 반복문에 자주 사용함

for i in range(1, 4) :
    print('날씨가 너무 추워요')

# 1~10까지 모든 정수 출력
# 임의읨 문자를 붙이면 쭈욱 나오게 할 수 있다
for i in range(1, 11):
    print(i)

for i in range(1, 11):
    print(i, end = ',')
# 1~100까지 모든 정수들의 합을 출력
a=0
for i in range(1, 101) :
    a = a + i
print(a)

b=0
for i in range(1, 101) :
    b = b + i
print(b)

# 1 ~ n까지의 합을 구하는 공식 : 가우스 덧셈 공식
# => (n * (n+1)) / 2
tot = (100 * (100 + 1)) / 2
print(tot)

#구구단 중 특정 단을 입력받아 출력
# 예를 들어 7단을 출력한다고 하면
dan = input('구구단 몇 단인지 입력하시오')
for i in range(1,10):
    print('{} X {} = {}'.format(dan, i, int(dan) * i))

# 2~8 사이 짝수 출력
for i in range(2,9,2):
    print(f'num = {i}')

ggg = []
for i in range(1, 11):
    ggg.append(i)
print(ggg)

for i in range(1, 12, 2):
    print(i, end=',')

for i in range(0,8,2):
    print(i, end=',')
# 단계를 감소로 해서 줄어들게 출력할 수 있음
for i in range(10, 1, -1):
    print(i, end=',')

# 시작값이 없는 range 함수
# 이럴 경우 기본값으로 0부터 함
print(list(range(1,10)))
print(list(range(10)))

# 이터러블에 문자열을 넣으면 아이템에는
# 문자열의 첫 문자부터 끝 문자가 순차적으로 저장됨
# 결과적으로 실행문은 문자 개수만큼 반복 실행됨

for c in 'Hello' :
    print(c, end=' ')

# 이터러블에 리스트를 넣으면 아이템에는
# 리스트를 구성하는 요소들이 순차적으로 저장됨
# 결과적으로 실행문은 리스트의 요소수만큼 반복 실행

menus = ['라면', '돈까스', '짜장면', '냉면', '정식']

for i in range(5):
    print(menus[i])

for i in range(len(menus)):
    print(menus[i])

for menu in menus:
    print(menu)
