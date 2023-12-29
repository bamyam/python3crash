# 컴프리헨션comprehension - 반복문 축약
# 다양한 데이터 객체에 사용되는 복잡한 구문을
# 단순하게 작성할 수 있도록 지원하는 기능

# 파이썬에는 4가지 종류의 축약을 지원
# list(py2), set(py3), dict(py3), generator(py3)

# 리스트에 적용하는 축약
# 1~10 까지의 정수를 리스트에 저장
a = list(range(1, 11))
print(a)

b = []
for i in range(1, 10+1):
    b.append(i)
print(b)

# 리스트 for 축약문
# [ 표현식 for 항목 in 반복가능객체]
c = [i for i in range(1, 11)]
print(c)

# 1 ~ 10까지 제곱값을 리스트로 생성하는 축약문 작성
d = [i ** 2 for i in range(1, 11)]
print(d)

# ex) 다음 리스트를 이용해서 제곱값을 계산하고
# 새로운 리스트에 생성하세요
val1 = [1, 2, 3, 4, 5]
val2 = [1, 2, 'A', False, 9, 100]

list1 = [i ** 2 for i in val1]
print(list1)

list2 = [i ** 2 if type(i) == int else i for i in val2]
print(list2)

# for if 축약문
# [ 표현식 for 항목 in 반복가능객체 if 조건]
# 여기서 else까지 같이 할려면 for 문 앞쪽의 표현식에 넣어야 함
list3 = [ i ** 2 for i in val2 if type(i) == int]
print(list3)

# 이건 불가능
list4 = [i ** 2 if type(i) == int for i in val2]
print(list4)

# 1~100 정수 중 홀수만 골라서 리스트에 저장
list5 = [i for i in range(1,101) if i % 2 == 1]
print(list5)

# 1 ~ 100 사이의 정수 중 임의의 정수가 짝수면 even,
# 홀수면 odd라고 구분해서 리스트에 저장하세요
list6 = []
for i in range(1, 101):
    if i % 2 == 1:
        list6.append('odd')
    else :
        list6.append('even')
print(list6)

# for 다중 if 축약문
# [ 표현식1 if 조건 else 표현식2 for 항목 in 반복가능객체]
list7 = ['odd' if i % 2 == 1 else 'even' for i in range(1,101)]
print(list7)

# 구구단 중 7, 8단의 결과를 리스트에 저장
list8 = []
for i in (7, 8):
    for j in range(1, 10):
        list8.append(i * j)
print(list8)

# 다중 for 축약문
# [ 표현식1 for 항목1 in 반복가능객체1 for 항목2 in 반복가능객체2]
list9 = [i * j for j in range(1, 10) for i in (7, 8)]
print(list9)

# name, grd 리스트의 값들을
#각각의 키와 값으로 딕셔너리를 만들어 저장하시오
name = ['혜교', '수지', '지현']
grd = ['우', '미', '수']

sj = {}
sj[name[0]] = grd[0]
sj[name[1]] = grd[1]
sj[name[2]] = grd[2]
print(sj)

# 반복문 버전
sj = {}
for i in range(len(name)):
    sj[name[i]] = grd[i]
print(sj)

# 딕셔너리 for 축약문 - {} 사용
# { 키값표현식 for key, val in
#                  zip(반복객체1, 반복객체2) }
# zip : 동일한 갯수의 시퀀스 자료형을 하나로
#       묶어주는 역할을 수행
# zip([1,2,3], ['a','b','c'])
# => [(1,'a'),(2,'b'),(3,'c')]

sj = { key:val for key, val in zip(name, grd)}
print(sj)

# 학생과 국어점수에 대한 리스트가 있을때
# 학생은 키로, 값은 합격여부로 하는 딕셔너리를 생성하세요
# 단, 국어점수가 85점이상인 경우 '합격',
#     그외는 '불합격'이라고 출력함
std = ['철수','영희','길동','꺽정']
kor = [50,80,90,60]
dict1 = {}
for i in range(len(std)):
    a = '불합격'
    if kor[i] >= 85:
        a = '합격'
    dict1[std[i]] = a
print(dict1)

for i in range(len(std)):
    if kor[i] >= 85:
        x = '합격'
    else :
        x = '불합격'
    dict1[std[i]] = x

print(dict1)

dict2 = {key: ('합격' if val >= 85 else '불합격') for key, val in zip(std, kor)}
print(dict2)

# 딕셔너리 for 축약문 - {} 사용
# { 키값 : 표현식1 if 조건 else 거짓일 때 표현식2 for key, val in zip(반복객체1, 반복객체2) }
results = {k: '합격' if v >= 85 else '불합격' for k, v in zip(std, kor) }
print(results)


