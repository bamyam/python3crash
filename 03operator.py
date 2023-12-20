# 수식expression
# 연산의 결과로 하나의 값이 되거나
# 특정 기능의 수행을 나타내는 표현들
# 수식 => 피연산자와 연산자로 구성
# 연산자 : 연산의 의미를 지닌 기호
# 피연산자 : 연산의 대상들을 의미

# 대입식 : 대입연산자를 이용한 수식(변수=수식)
a=10
b=20
c=30
print(a,b,c)

#대입식을 한줄에 나타내려면 ;를 사용
d = 10; e = 20; f = 30

print(d,e,f)

#다중 할당 : 여러 변수의 값을 한번에 할당 - ,(콤마)를 사용
g, h, i = 20, 30, 40
print(g, h, i)

#정수 대입시 자릿수를 의미하는 구분자 지정 : _(언더바)를 사용, 출력할 때는 언더바가 보이지 않음
j = 1_000_000_000  # 10억
#j = 1000000000

print(j)

# 상수 정의
# 프로그램 실행 중에 언제나 동일한 값을 유지하는 변수
# 상수의 이름은 대문자료 표시

PI = 3.14152

print(PI)

#산술식 : 산술연산자(+, -, *, /)를 이용한 수식
#파이썬에서는 //, %, **도 지원
print(10 / 3, 10 % 3, 10 // 3) # 나누기, 나머지, 몫을 구하는 연산
print(10**1.10**2, 10**3)  # ?궁금쓰

#관계식 : 관계연산자(대소, 순서관계)를 이용한 수식
#수식의 결과는 TRUE, False로 출력
print(10>3, 10<=3, 10==3)

# 논리식 : 논리연산자(논리합/곱/부정)를 이용한 수식
# 또한, 둘 이상의 논리식이나 관계식으로 구성된 수식
# 논리식의 경우, 수식의 구성에 따라 단축식 평가short-circuit가 가능
#and(&)는 앞에가 False면은 뒤가 무엇이든 False이므로 앞의 수식만 보고 결과를 판단
#or(|)는 앞에가 True면은 뒤가 무엇이든 True이므로 이처럼 앞에만 보고 판단하는 것이 short-circuit
#and, or이 같이 왔을 때 and(&)를 먼저 수행

#and 연산시 첫번째 수식의 결과가 F면 단축식 평가를 적용해서 F
print((5==3) and (5 > 3)) # 5==3이 false이기 때문에 뒤에가 True더라도 결과는 False임

#or 연산시 첫번째 수식의 결과가 T면 단축식 평가 적용 - T
print((5 != 3) or (5 == 3))

#복합 대입연산자 : 대입연산자와 산술연산자를 결합한 수식
#보통 수식을 간단히 작성 시 사용 - 축약표현
#변수 = 변수 + 수식 => 변수 += 수식

k=10
k = k + 1
k += 1
print(k)

# 연산자 우선순위
# 괄호내 연산자 -> 단항연산자 -> 산술연산자 -> 관계연산자 -> 논리연산자

# 연산자의 부수적인 기능 - 문자열 연산
# + : 문자열 연결concatenate
# * : 문자열 반복repeat 연결
str1 = 'Hello, '
str2 = 'world!!'
print(str1+str2)

print(str1 * 3)
print(3* str2)

# 단, 숫자와 문자열에 +연산을 시도하면? - 오류가 발생하므로 형변환이 필요
# 문자열을 숫자로 변환 : int(), float() 이용
# 숫자를 문자로 변환 : str() 이용
print(123 + '456') #에러가 뜸
print(123 + int('456')) # 문자를 숫자로 변환
print(str(123) + '456') #숫자를 문자로 변환

#숫자형과 문자형의 논리 연산
# 0 또는 빈 문자열은 False로 인식
# # bool 함수를 이용하면 지정한 값의 논리값을 알 수 있음
print(bool(0), bool(''))
print(bool(1), bool('abc'))

#다음 수식의 결과는?
print(0 and 'abc', 1 and 'abc') # ?결과가 이해 안됨
print('' or 'abc', '' and 'abc') # ? 결과가 이해 안됨

#문자열 서식하기formatting하기
# 문자열 \에서 특정 부분만 바뀌고 나머지는 변화가 없는 경우
# 문자열 서식화라ㅡㄹ 이용하면 편리하게 작용가능
print('이름 : 홍길동, 나이 : 25')
name, age = '홍길동', 25
print('이름 :', name, ', 나이 :', age)

# % 서식 - 서식문자열 사용
print('이름 : %s, 나이 : %d' % (name, age))

# .format
print('이름 : {}, 나이 : {}'.format(name, age))

# f-string
print(f'이름 : {name}, 나이 : {age}')

number = 1

print('7 X', number, '=', number * 7)
number = 7
print('7 X %d = %d' % (number, number * 7))
print('7 X {} = {}'.format(number, number * 7))
number = 7
print(f'{number} X 1 = {number * 1}')
print(f'{number} X 2 = {number * 2}')
print(f'{number} X 3 = {number * 3}')
print(f'{number} X 4 = {number * 4}')
print(f'{number} X 5 = {number * 5}')
print(f'{number} X 6 = {number * 6}')
print(f'{number} X 7 = {number * 7}')
print(f'{number} X 8 = {number * 8}')
print(f'{number} X 9 = {number * 9}')

for i in range(1, 10) :
    print(f'{i} X 7 = {i*7}')