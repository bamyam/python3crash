# Whlie 만
# 조건을 만족할 때까지 반복을 실행
# 변수 = 초기값
#while 조선식:
#   반복할 문장
    # 변수 증가 / 감소

# 1~10까지 모든 정수 출력
# for i in range(1, 10+1):
#   printI(i, end=' )
i = 1            #반복초기값
while i <= 10:   # 반복 종료조건
    print(i, end=' ')
    i = i + 1

# 1~ 50까지 모든 정수 중 홀수만 출력
i = 1
while i <= 50:
    print(i, end=' ')
    i = i + 2

i = 1
while i <= 50:
    if i % 2 != 0:print(i, end=' ') # 선생님 풀이_홀수만 출력하기
    i = i + 1

# 1 ~ 50까지 모든 정수 중 7의 배수만 출력
i = 7
while i <= 50:
    print(i, end=' ')
    i = i + 7

i = 1
while i <= 50:
    if i % 7 == 0:print(i, end=' ') # 홀수만 출력하기
    i = i + 1

# 1 ~ 200까지 모든 정수의 합 출력
i = 1
a = 0
while i <= 200:
    a = a + i
    i = i + 1
print(a)

# 0 ~ 100까지 3과 8의 공배수와 최소공배수를
i = 1
mincm = 0
while i <= 100:
    if i % 3 == 0 and i % 8 == 0:
        print(f'3과 8의 공배수 : {i}')
        if mincm == 0 : mincm = i #최소 공배수 저장
    i = i + 1
print(f'3과 8의 최소공배수 : {mincm}')

# 반복문 내 실행중지 : break
# for, while문 내에서 반복흐름을 벗어나기 위해 사용
# 1~10000까지의 정수 합을 출력
#단, 정수합이 12345보다 크면 계산을 중단하기

sum = 0

for i in range(1, 10000):
    if sum > 12345678 :
        print(i, sum)
        break # 반복중단
    sum = sum + i

print(sum)

# while문으로 출력
sum = 0
i = 1
while sum <= 12345678:
    sum = sum + i
    i = i + 1
print(i, sum)

# 반복문 내에서 반목 건너뛰기 : continue
# for, while문 내에서 반복흐름을 일시적으로 넘기기 위해 사용

# 1부터 100까지의 정수 합을 출력
# 단, 3의 배수나 7의 배수는 제외하고 합을 계산하세요
sum = 0
for i in range(1,101):
    if i % 3 == 0 or i % 7 == 0:
        continue
    sum = sum + i
print(sum)

i = 0
sum = 0

while i < 100:
    i = i + 1 # i=i+1이 if문 밑에 있으면 실행이 안 됨
    if i % 3 == 0 or i % 7 == 0: continue
    sum = sum + i


print(sum)

# 1 ~ 99 사이에서 3/6/9가 있으면 짝!이라 출력하기
for i in range(1,100):
    print(i, end=' ')
    for j in str(i):
        if j in ('3', '6', '9'):
            print('짝!', end=' ')
    print()

# 선생님 풀이
# 간단하게 짝 하나만 나오게 하는 버전
for i in range(1, 99+1):
    if '3' in str(i) or '6' in str(i) or '9' in str(i):
        print(i, '짝!')
# 완전버전 - 근데 이러면 33, 66, 99를 인식하지 못함
for i in range(1, 99+1):
    print(i, end=' ')
    if '3' in str(i) : print('짝!', end=' ')
    if '6' in str(i) : print('짝!', end=' ')
    if '9' in str(i) : print('짝!', end=' ')
    print()
# 완전버전에서 출력을 다듬은 내용
for i in range(1, 99+1):
    jjak = ''
    if '3' in str(i) : jjak += ' 짝!'
    if '6' in str(i) : jjak += ' 짝!'
    if '9' in str(i) : jjak += ' 짝!'
    print(f'{i} {jjak}')
# 33, 66, 99 안되는 내용 해결
for i in range(1, 99+1):
    jjak = ''
    if '3' in str(i) : jjak += ' 짝!'
    if '6' in str(i) : jjak += ' 짝!'
    if '9' in str(i) : jjak += ' 짝!'
    if i == 33 or i == 66 or i == 99: jjak += ' 짝!'
    print(f'{i} {jjak}')
# 다른 버전_자바 스타일
for i in range(1, 99+1):
    if i <= 9: # 1~9사이 3/6/9 찾기는 3으로 나누면 0이 되는것만 찾으면 됨
        if i % 3 == 0 : print(i, '짝!')
        else : print(i)
    else:      # 10~99사이 3/6/9 찾기는 개별글자가 3/6/9인지 찾아야 함
        print(i, end='')
        num1 = int(str(i)[0])
        num2 = int(str(i)[1])
        if num1 % 3 == 0:print(' 짝', end='')
        if num2 != 0 and num2 % 3 == 0:print(' 짝', end='')
        print()

# 오전 9시 ~ 오후 6시까지 열차 교차시간 알아내기
#시간 = 전체시간을 60으로 나눴을 때 몫
#분 = 전체시간을 60으로 나눴을 때 나머지
# 교차시간은 공배수 문제
for i in range(541, 1081):
    if (i-540) % 10 == 0 and (i-540) % 25 == 0:
        print(f'{i // 60}시 {i % 60}분')
    elif (i-540) % 10 == 0 and (i-540) % 30 == 0:
        print(f'{i // 60}시 {i % 60}분')
    elif (i-540) % 25 == 0 and (i-540) % 30 == 0:
        print(f'{i // 60}시 {i % 60}분')

# 관리자 로그인 기능
# 암호입력 -> 암호가 맞는지 확인 -> 암호가 틀렸다면 암호 확인 메시지 출력 -> 5회 이상 실패시 실패초과
passwd = 'hanbitac'
loginCnt = 0
while True :
    identi = input('관리자 암호를 입력하세요.')
    if identi == passwd:
        print('로그인 됐습니다.')
        break
    else :
        loginCnt = loginCnt + 1
        if loginCnt == 5:
            print('로그인 실패!! 횟수초과!!')
            break
        print('암호를 다시 확인하세요!')

# 선생님 풀이
passwd = 'hanbitac'
loginCnt = 1
while True:
    if loginCnt > 5:
        print('로그인 실패! 입력횟수 초과')
        break
    pwd = input('관리자 암호를 입력하세요')

    if passwd != pwd:
        print('암호를 다시 확인하세요!')
        loginCnt += 1
    else:
        print('로그인 되었습니다!')
        break
