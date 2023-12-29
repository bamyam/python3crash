# 함수와 모듈
# 함수는 일정한 작업을 수행하는 코드 집합체
# 보통 여러 곳에 반복적으로 사용되는 코드들을 함수로 정의해서 사용

# 즉, 여러 곳에 반복적으로 사용할 가치가 있는 코드를 한 뭉치로 묶고
# (어떤 입력값을 주면) 결과가 반환되도록 사용

# 또한, 여러 코드들을 함수화하면 프로그램의 흐름을
# 일목요연하게 파악하기 쉬움

# 코드의 이식성이나 재사용성이 높아짐 - 개발 속도가 빨라짐

# 다른 사람과의 협업시 코드가 섞이지 않게 하기 위한
# 목적도 있음 - 모듈

# 함수 정의
# def 함수명(매개변수):
#     함수몸체(코드들)

print('선생님 미워요') # 단순출력

print('선생님 미워요') # 반복출력
print('선생님 미워요')
print('선생님 미워요')
print('선생님 미워요')

for _ in range(3):   # 개선된 반복
    print('선생님 미워요')

# 이러한 반복문을 여러번 사용해야 한다면?
# 또 만약, '미워요' 대신 '싫어요'나 '좋아요'로 바꿔야 한다면?
# => 함수를 이용!

# 함수의 유형
# 입력값 x   반환값 x
# 입력값 x   반환값 o   !!
# 입력값 o   반환값 x
# 입력값 o   반환값 o   !!!

def saymsg(): # 입력값x, 함수 내에서 출력처리(반환값x)
    for _ in range(3):  # 개선된 반복
        print('선생님 미워요')

# 함수 호풀
# 함수명(), 함수명((입력값)
saymsg()

def saymsg2():
    msg = ()
    for _ in range(3):  # 개선된 반복
        print('선생님 {msg}')

def saymsg3(msg): # 입력값 o, 함수 내에서 출력처리(반환값x)
    for _ in range(3):
        print(f'선생님 {msg}!')
saymsg3('좋아요')
saymsg3('싫어요')
saymsg3('미워요')

def sensoroOn():
    print('온도센서 작동을 시작한다.')
def sensoroOff():
    print('온도센서 작동을 중지한다.')

def notebookSize():
    cm = int(input('길이를 입력하세요.(cm)'))
    inch = cm * 0.393701
    return f'{cm:.1f}cm = {inch:.4f} inch'

print(notebookSize())

def calDist():
    dist = ''
    time = int(input('이동시간을 입력하세요'))
    speed = int(input('이동속도를 입력하세요'))
    dist +=  f'이동 거리는 {time * speed :.1f}km 입니다.'
    return dist
print(calDist())

def calculator ():
    num1 = int(input('숫자를 입력하세요.'))
    opt = input('연산자를 선택하세요. 1.덧셈, 2.뺄셈, 3.곱셈, 4.나눗셈')
    num2 = int(input('숫자를 입력하세요.'))
    if opt == '1':
        print(f'덧셈 결과 :  {num1 + num2}')
    elif opt == '2':
        print(f'뺄셈 결과 :  {num1 - num2}')
    elif opt == '3':
        print(f'곱셈 결과 :  {num1 * num2}')
    elif opt == '4':
        print(f'나눗셈 결과 :  {num1 / num2}')
    else :
        print('연산자를 잘못 선택하셨습니다.')

calculator()

def saymsg4(msg): # 입력값 o, 처리결과 반환 (반환값 o)
    text = ''
    for _ in range(3):
        text += f'선생님 {msg}!\n'
    return text # 결과를 처리하지 않고 넘김

print(saymsg4('미워요'))

def notebookSize2():
    cm = int(input('길이를 입력하세요.(cm)'))
    inch = cm * 0.393701
    return inch
# 결과값만 넘겨서 나중에 수정할 때 바로 수정할 수 있게 함
# 국제화 트랜드에 맞춰서 출력을 자유롭게 변경할 수 있도록 값만 넘김
print(f'{notebookSize2()} inch')
print(f'{notebookSize2()} 인치')

# 하지만 입력값도 보이게 하고 싶기에 return에 입력값 넣기
def notebookSize3():
    cm = int(input('길이를 입력하세요.(cm)'))
    inch = cm * 0.393701
    return cm, inch
# 뒤에서 notebookSize3()의 값이 2개 나오므로 변수 2개를 선언해서 받아주는 것
cm, inch = notebookSize3()

print(f'{cm}cm = {inch:.4f} inch')
print(f'{cm}센티미터 = {inch:.4f} 인치')

def calDist2():
    time = int(input('이동시간을 입력하세요'))
    speed = int(input('이동속도를 입력하세요'))
    dist =  time * speed
    return time, speed, dist
time, speed, dist = calDist2()
print(f'{time} {speed} {dist}')



def func1(a, b):
    print(f'덧셈 결과 :  {a + b}')
def func2(a, b):
    print(f'뺄셈 결과 :  {a - b}')
def func3(a, b):
    print(f'곱셈 결과 :  {a * b}')
def func4(a, b):
    print(f'나눗셈 결과 :  {a / b}')
def calculator2 ():
    num1 = int(input('숫자를 입력하세요.'))
    opt = input('연산자를 선택하세요. 1.덧셈, 2.뺄셈, 3.곱셈, 4.나눗셈')
    num2 = int(input('숫자를 입력하세요.'))
    if opt == '1':
        func1(num1, num2)
    elif opt == '2':
        func2(num1, num2)
    elif opt == '3':
        func3(num1, num2)
    elif opt == '4':
        func4(num1, num2)
    else :
        print('연산자를 잘못 선택하셨습니다.')

calculator2()

op1 = int(input('숫자를 입력하세요'))
op2 = input('연산자를 선택하세요. 1.덧셈, 2. 뺄셈, 3.곱셈, 4.나눗셈')
op3 = int(input('숫자를 입력하세요.'))

result = 0
if op2 == '1' :
    result = op1 + op3
    op2 = '덧셈'
elif op2 == '2' :
    result = op1 - op3
    op2 = '뺄셈'
elif op2 == '3' :
    result = op1 * op3
    op2 = '곱셈'
elif op2 == '4' :
    result = op1 / op3
    op2 = '나눗셈'

print(f'{op2} 결과 : {result:.1f}')

# 솔리드

def readData():
    op1 = int(input('숫자를 입력하세요'))
    op2 = input('연산자를 선택하세요. 1.덧셈, 2. 뺄셈, 3.곱셈, 4.나눗셈')
    op3 = int(input('숫자를 입력하세요.'))
    return op1, op2, op3


def computeNumber(op1, op2, op3):
    result = 0
    if op2 == '1':
        result = op1 + op3
        op2 = '덧셈'
    elif op2 == '2':
        result = op1 - op3
        op2 = '뺄셈'
    elif op2 == '3':
        result = op1 * op3
        op2 = '곱셈'
    elif op2 == '4':
        result = op1 / op3
        op2 = '나눗셈'
    return op2, result


def computer():
    # 데이터 입력부
    op1, op2, op3 = readData()
    # 데이터 계산
    op2, result = computeNumber(op1, op2, op3)
    # 데이터 결과
    return op2, result

op2, result = computer()
print(f'{op2} 결과 : {result:.1f}')

# 함수에 값 전달하기
# 매개변수 parameter : 함수 정의시 함수에서 사용할 변수 정의
# 매개변수는 함수 호출 시 전달받은 인수로 초기화되어 사용됨
# 인수 argument  : 함수 호출시 매개변수로 넘겨주는 데이터

# return : 실행이 끝난 후에 나온 결과물을 호출부로 반환할 수 있음,
# 또는 함수 실행을 종료할 수 있는 기능

def convertUnit():
    mm = int(input('길이(mm)를 입력하세요.'))
    print(f'{mm}mm --> {mm * 0.1} cm')
    print(f'{mm}mm --> {mm * 0.001} m')
    print(f'{mm}mm --> {mm * 0.03937} inch')
    print(f'{mm}mm --> {mm * 0.003281} ft')

convertUnit()

def readMM():
    mm = int(input('길이(mm)를 입력하세요.'))
    return mm

def convertAll(mm):
    cm = mm * 0.1
    m = mm * 0.001
    inch = mm * 0.03937
    ft = mm * 0.003281
    return mm, cm, m, inch, ft

def convertUnit2():
    mm = readMM()
    return convertAll(mm)

mm, cm, m, inch, ft = convertUnit2()
print(f'{mm}mm --> {cm} cm')
print(f'{mm}mm --> {m} m')
print(f'{mm}mm --> {inch} inch')
print(f'{mm}mm --> {ft} ft')

hanbitMenus = {'쌀': 9900, '상추': 1900, '고추': 2900, '마늘': 8900, '통닭': 5600, '햄': 6900, '치즈': 3900}
def hanbitSale():
    print('---------------------------------------')
    print('-- 한빛마트 오늘의 할인 가격표 출력 시스템 --')
    print('---------------------------------------')
    sale = int(input('오늘의 할인율을 입력하세요.'))
    for menu in hanbitMenus.keys():
        print(f'{menu:4s} : {hanbitMenus[menu]:4d} 원 {sale:2d} %DC -> {hanbitMenus[menu] * ((100 - sale)/100):.0f} 원')
    print('---------------------------------------')

hanbitSale()





