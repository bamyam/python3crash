# 튜플 자료형
# 순차적 데이터를 관리하는 자료형(순서가 존재)
# 리스트와 동일하지만, 변경 불가능 특성을 지님
# => 생성은 가능 / 추가,수정,삭제는 불가능
# 튜플 객체 생성은 ()를 사용

tuple1 = ()
tuple2 = (1, 2, 3, 4, 5)
tuple3 = ('a', 'b', 'c', 'd')
tuple4 = (1, 'a', 2.14, "d", 5)

print(tuple4)

# 튜플 추가 / 수정 / 삭제 해보기 -리스트와 차이점
tuple1.append(10)
tuple2[4] = 10
tuple2.pop()
tuple2.remove(3)

# 튜플 합치기 : +만 지원 -리스트와 차이점
print(tuple2 + tuple3)
tuple2.extend(tuple3) # 이건 안 됨

# 만약, 튜플의 요소를 변경해야 한다면?
# 튜플을 리스트로 변환한 후 요소를 변경하고
# 다시 리스트를 튜플로 변환하면 됨
# 튜플을 리스트로 변환 : list(대상)
# 리스트를 튜플로 변환 : tuple(대상)
# 튜플을 변경할 수 있는 방법이 있음
tuple1 = list(tuple1)
tuple1.append('A')
tuple1.append('B')
tuple1= tuple(tuple1)
print(tuple1)

#리스트/튜플의 요소 인덱스 알아내기 : index(값)
tuple4.index(2.14)
tuple4.index('d')

# 튜플의 아이템 정렬 : sorted()함수
# 하지만 반환되는 값의 자료형은 리스트

#연습문제
numbers = (10, 20, 30, 40, 50, 60)
print(numbers[1:3])
print(numbers[:2])
print(numbers[1:4])
print(numbers[3: len(numbers)-1])

# 난수 생성하기
# random이라는 모듈이 필요
# random()    : 0~1사이 임의의 부동소수점 숫자 출력
# randint(x,y) : x~y사이 임의의 정수 출력
# randrange(s,e,l) : 시작부터 끝 사이 임의의 출력

import random as rnd

print(rnd.random())
print(rnd.randint(1, 10)) # 값이 다 다르게 나옴

# seed와 같이 실행하면 같은 값이 나옴
rnd.seed(2312271045)
print(rnd.random())
print(rnd.randint(1, 10)) # 1 ~ 10 사이 난수 생성

print(rnd.randrange(1,10)) # 1 ~ 9 사이 난수 생성

# 1 ~ 100 사이 임의의 3의 배수 출력
print(rnd.randrange(3,100, 3))

# 1 ~ 45 사이 임의의 정수 6개를 추출해서
# 리스트와 튜플에 저장하는 코드를 작성하세요
list1 = []
tuple1 = ()
for _ in range(6):
    list1.append(rnd.randint(1, 45))
print(list1)

tuple1 = list(tuple1)
for _ in range(6):
    tuple1.append(rnd.randint(1, 45))
tuple1 = tuple(tuple1)
print(tuple1)

list2 = [1, 2, 3]
list3 = [2, 4]
print(len(list2) or len(list3))

# 1 ~ 45 사이 임의의 정수 6개를 추출해서
# 리스트와 튜플에 저장하는 코드를 작성하세요
# 단, 값이 중복되지 않도록

# 실패작
import random as rnd
list1 = []
tuple1 = ()
tuple1 = list(tuple1)
list1.append(rnd.randint(1, 45))
tuple1.append(rnd.randint(1, 45))
while True :
    for i, j in zip(list1, tuple1): # rnd를 변수에 안 넣고 그냥 다루면 같은 수만 나옴
        print(i, j)
        if i not in list1 and len(list1) < 7:
            list1.append(rnd.randint(1, 45))
        if j not in tuple1 and len(tuple1) < 7:
            tuple1.append(rnd.randint(1, 45))
        else :
            continue
    if (len(list1) and len(tuple1)) == 6:
        break
tuple1 = tuple(tuple1)
print(tuple1, list1)

# 다시 한 개선작
# for문으로 하나하나 분해하기보다 in으로만 해도 충분히 확인가능하기 때문에 for문을 빼고
# random값을 변수에 담음
list1 = []
tuple1 = ()
tuple1 = list(tuple1)
while True :
    lotto2 = rnd.randint(1, 45)
    lotto3 = rnd.randint(1, 45)
    if lotto2 not in list1 and len(list1) < 7:
        list1.append(lotto2)
    if lotto3 not in tuple1 and len(tuple1) < 7:
        tuple1.append(lotto3)
    else :
        continue
    if (len(list1) and len(tuple1)) == 6:
        break
tuple1 = tuple(tuple1)
print(list1, tuple1)

# 선생님 풀이
import random as rnd
lottos = []
cnt = 0
while len(lottos) < 6:
    cnt += 1
    lotto = rnd.randint(1, 45)
    if lotto not in lottos:
        lottos.append(lotto)

print(lottos, cnt)
