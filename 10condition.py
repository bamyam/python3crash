# 조건문
# 주어진 상황에 따라 적절한 명령문을 수행하는 문장
# 프로그래밍에서 조건을 판단하여
# 해당 조건에 맞는 상황을 수행하는데 사용됨

# 조건문 작성시 반드시 들여쓰기(탭)에 따라 문장을 작성해야 함
# 조건문은 일반적으로 비교연산자나 논리연산자를
# 이용한 표현식으로 구성
# 비교연산자 : x > 100, y != 123
# 논리연산자 : (x > 100) and (y != 123)

# 조건연산자
# 일반적인 조건문(if ~ else)을 한 줄로 표현한 것
# 조건식이 참일 때 if
# 조건식의 결과가 거짓일 때 else

# 수입, 지출을 입력받아 흑자/적자 여부 출력
# 입력
income = int(input('수입은? :'))
outcome = int(input('지출은? :'))
#처리
result = '흑자' if income > outcome else '적자'
#출력
print(f'{income} {outcome} {result}')

#긴급재난지원금 대상자 판별
# 입력 - 월소득, 지원금 중첩여부 확인
income = int(input('월 소득을 입력하세요. : '))
supFund = int(input('다른 지원금을 받고 있습니까? 1번 받고 있다, 2번 받고 있지 않다. '))

#처리 - 월소득이 4,000,000원 이하, 다른 지원금을 받지 않는 세대 판별
result_income = True if income < 4_000_000 else False
result_supFund = True if supFund == 2 else False
result = '수급대상자' if result_income and result_supFund else '수급대상자 아님'
#선생님이 하신건데 이게 더 깔끔하고 괜찮을 듯
total_result = '수급대상자' if income < 4_000_000 and supFund == 2 else '수급대상자 아님'

# 결과출력
print(result)

# 처리 할 때 한꺼번에 처리하기 - 가독성이 떨어지는 듯
result_4 = '수급대상자' if (True if income < 4_000_000 else False) and (True if supFund == 2 else False) else '수급대상자 아님'
print(result_4)

#모듈
# 타인이나 조직이 만든 특정 기능을 모아놓은 파일 (재사용이 용이하게 하는 것이 목적)
# 모듈을 사용하려면 import 키워드 사용

# operator 모듈 사용하기
# 연산자를 사용했을 때보다 실행 속도가 빠름
# add/sub/mul/truediv/mod/floordiv/pow
# eq/ne/gt/ge/lt/le
# and_/or_/not_

import operator as op
import math

# result = (income < 4_000_000) and (supFund == 2)
result = op.and_(op.le(income, 4_000_000),
                  op.eq(supFund, 2))

# 업무 컴퓨터 수량 파악
# 3대의 컴퓨터 8시간을 일하면 하루 업무 처리 가능
# 근무시간이 늘면 컴퓨터 수량이 줄어들어야 함
# 방정식으로는 computer * time = 3 * 8

# 입력 - 실패 : 반비례한다는 성질을 알지 못함
# workTime = int(input('근무시간을 입력하세요 :'))
# capPerOne = op.truediv(8, 3)

#처리
# nesQuan = math.ceil(op.truediv(workTime, capPerOne))

#출력
# print(f'필요한 컴퓨터 : {nesQuan}')

workTime = int(input('근무시간을 입력하세요 :'))
coms = op.truediv(3 * 8, workTime)
print(f'필요한 컴퓨터 : {coms:.0f}')

# 780달러와 650유로 노트북 중
# 달러로 구매했을때와 유로로 구매했을때
# 어느 것이 더 싼지 알아보세요
# 단, 2023.12.22 기준 환율을 적용하세요

# 달러와 유로로 구매했을 때 원이 얼마나 필요한지 환율을 통해 구하고
# 그 값이 싼 쪽을 파악해서 출력하기

# 입력 - 달러와 유로 환율, 각 물품별 필요한 달러와 유로
prdDol = int(input('구매하고자 하는 물품은 몇 달러인가요?'))
prdEur = int(input('구매하고자 하는 물품은 몇 유로인가요?'))
rateExcDol = int(input('오늘의 미국환율 : '))
rateExcEur = int(input('오늘의 유로환율 : '))

dlrnb = op.mul(prdDol, rateExcDol)
errnb = op.mul(prdEur, rateExcEur)

# 처리
result = '유로로 구매하세요' if op.ge(dlrnb, errnb) else '달러로 구매하세요'
print(f'달러로 구매 시 비용은 {dlrnb}원이며, 유로로 구매 시 비용은 {errnb}원이므로, {result}')
