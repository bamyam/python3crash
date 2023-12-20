#1
# 프로그래밍 언어 실습 시 글꼴은 고정폭 글꼴을 사용할 것을 추천!
print('''
*   *    **    ****    ****   *   *      /////
*   *   *  *   *   *   *   *  *   *     | o o |
*****  *    *  ****    ****    * *     (|  ^  |) 
*   *  ******  *   *   *   *    *       | [_] |  
*   *  *    *  *    *  *    *   *        -----
''')

print('            +---+')
print('            |   |')
print('        +---+---+')
print('        |   |   |')
print('    +---+---+---+      /\_/\      -----   ')
print('    |   |   |   |     ( \' \' )   / Hello \ ')
print('+---+---+---+---+     (  -  )  <  Junior |')
print('|   |   |   |   |      | | |    \ Coder!/ ')
print('+---+---+---+---+     (__|__)     -----   ')

#학생 테이블의 각 컬럼 데이터도 변수로 선언하고 값으로 초기화
stno = 1
hakbun = 201350050
name = '김태희'
addr = '경기도 고양시'
bitrh = '1985.3.22'
deptid = 1
profid = 4
regdate = '2023-12-20 14:43:15'

print(stno, hakbun, name, addr, birth)
print(stno, deptid, profid,)

#3
rate1 = 1
long = 2 # 자바에서는 long이 숫자 자료형의 하나를 나타내는 예약어이기 때문에 변수로 사용이 불가
TimeLimit = 3
numberOfWindows = 4

#4
x=1; y=6
s0, v0, t, g = 4, 5, 6, 9.8
print(3*x)
print(3*x + y)
print((x + y) / 7)
print((3 * x + y) / (z + 2))
print(s0 + v0 * t + 1/2 * g * t**2)

#5
print(1 / 3, (1/3) * 3) # 부동소수점 연산의 헛점이 원인
print(7 / 3, 7 % 3, 7 // 3)
result = 2
result /= 2 # result = result / 2
print (result) # 결과가 1이 나와야 하지만 1.0이 나옴

#6
x = 2.5;  y = 1.5; m = 18;  n = 4
print(x + n * y - (x + n) * y) #-1.25
print(m / n + m % n) # 6.5
print(5 * x - n / 5) # 11.7
print(1 - (1 - (1 - (1 - (1 - n))))) # -3
#7
print(3 + 4.5 * 2 + 27 / 8)
print(True | False & 3 < 4 | (not(5==7)))
    print(not(5==7))
    True | False & 3 < 4 | (not(5==7))
    True | False & 3 < 4
    3 < 4 | (not(5==7))
print(True | (3 < 5 & 6 >= 2))
print((not True) > bool('A'))
print(not True > bool('A')) #not 보다 >와 같은 비교 연산자가 우선순위가 있어 비교연산자를 먼저 계산함
print(7 % 4 + 3 - 2 / 6 * bool('Z'))
bool('Z')
print(bool('D') + 1 + bool('M') % 2 /3)
print(1 + 1 + 1 % 2 /3)
print(5.0 / 3 + 3 / 3)
print(53 % 21 < 45 / 18)
print((4 < 6) | True & False | False & (2 > 3))
print(True | True & False | False & False) #??? False아님 / and를 먼저 수행함
print(7 - (3 + 8 * 6 + 3) - (2 + 5 * 2))
#9
print(True & False & True | True)
print(True | True & True & False)
print((True & False) | (True & (not(False))) | (False & (not(False))))
print((2 < 3) || (5 > 2) && !(4 == 4) || 9 != 4)
print(6 == 9 || 5 < 6 && 8 < 4 || 4 > 3)

#10
print(27 / 13 + 4)
print(27 / 13 + 4.0)

print(23 / 5 + 23 / 5.0)
print(42.7 % 3 + 18)

print(2.0 + bool('a')) # 문자와 실수 간 산술 연산 불가
print(2 + bool('a'))

print('a' + 'b')

print(bool('a') / bool('b')) # 문자끼리 산술연산 불가
print(float(bool('a') / bool('b')))

#논리식과 산술식이 결합된 수식에서는
#논리식의 결과가 True라면 값이 출력
#논리식의 결과가 False라면 False가 출력
print((3 < 4) and 5 / 8)
print((3 > 4) and 5 / 8)
print('a' and not 'b')
#11
name = '홍길동'
weight = 32.5
age = 19
print(name, weight, age)

#12
# k - 나이
# 세는 나이 : 출생 시 1살, 해가 지나면 +1
# 만나이 : 출생 시 0살, 생일이 지나면 +1
# 연나이 : 현재년도 - 출생연도
birthYear = 2005
currentYear = 2023

age = currentYear - birthYear
print('연나이 :', age)

#13
print('7 X 1 = 7')
print('7 X 2 = 14')
print('7 X 3 = 21')
print('7 X 4 = 28')
print('7 X 5 = 35')
print('7 X 6 = 42')
print('7 X 7 = 49')
print('7 X 8 = 56')
print('7 X 9 = 63')

