# 파이썬 자료구조
# 자료구조는 대량의 데이터를
# 효율적으로 저장,조회,수정,삭제하기 위해
# 요구되는 기능과 기법을 의미
# 대표적인 자료구조 : 리스트, 튜플, 셋, 딕셔너리

# 성적프로그램 v2
# 이름,국어,영어,수학을 이용해서
# 총점,평균,학점을 처리하고 결과출력
# 단, 3명의 학생에 대해 성적처리를 진행함
# 변수 초기화
name1, name2, name3 = '혜교', '지현', '수지'
kor1, kor2, kor3 = 99, 65, 75
# ...
# 처리할 데이터 갯수에 따라 변수를 일일이 선언해야 함 - 불편!

# tot1 = kor1 + eng1 + mat1
# tot2 = kor2 + eng2 + mat2
# tot3 = kor3 + eng3 + mat3
# ...
# 성적처리시에도 동일한 코드를 여러번 반복해 작성함 - 번거로움
# => 이러한 문제를 해결하기 위해 자료구조와 관련된 기술을 사용

# 리스트list
# 다른 프로그래밍 언어에서는 배열array과 유사
# 동일한(동일하지 않은) 형식의 데이터를
# 1차원 형태로 순차적으로 저장하는 자료구조 (중복 허용)
# 선언방법은 값들을 []안에 정의하고 사용
# 리스트의 각 요소에 접근(참조)하려면 변수[인덱스] 형식을 사용

fruits = ['사과', '포도', '수박', '참외', '배', '자두', '복숭아', '바나나']
print(fruits)

# 저녁 메뉴를 리스트로 선언
menus = ['라면', '돈까스', '짜장면', '냉면', '정식']
print(menus)

# 리스트에서 일부 요소element, item만 출력
# 단, 첫번째 요소의 위치값index은 0임
print(menus[0:3])
print(menus[5]) # 오류발생!

# 동적으로 리스트 생성하기
menus = []

# 리스트에 요소를 추가하려면 append함수 사용
# 추가된 요소는 리스트의 맨 뒤에 부착 - FIFO(First In First Out)
menus.append('라면')
menus.append('돈까스')
menus.append('짜장면')
menus.append('우동')
menus.append('정식')

print(menus)

# 지정한 위치에 새로운 요소 추가  : insert(위치, 값)
# 지정한 위치에 이미 값이 존재한다면 그 값은 뒤로 밀림
menus.insert(2, '냉면')

#리스트 요소 수정 : 리스트명[위치] = 새로운 값
menus[3] = '탕수육'

# 리스트 요소 삭제 1 : remove(값) - 값으로 삭제
menus.remove('탕수육')

# 리스트 요소 삭제 2 : pop(위치) - 위치로 삭제
# 지정한 위치 뒤에 값이 존재한다면 그 값은 앞의 칸으로 당겨짐
menus.pop(2)

# 리스트 요소 삭제 3 : pop() - 위치로 삭제, 맨 뒤의 요소 삭제
menus.pop()

# 리스트로 다양한 데이터 다루기
sjs = []
sj = ['해교', 65, 76, 87]
sjs.append(sj)
sj = ['지현', 22, 77, 97]
sjs.append(sj)
sj = ['수지', 66, 77, 88]
sjs.append(sj)

print(sjs)
print(sjs[0])

#참석자 명단 선언
attendList = ['이순철', '김병헌', '김민우', '박찬호', '김민태']

#참석자 수 확인 : len
len(attendList)

#문자열에 len 함수 적용시 문자열의 길이 출력
str = 'Hello, World!!'
print(len(str))

#사용자로부터 데이터 입력받기 : input
#input 함수로 입력받은 데이터는 무조건 문자열로 처리됨
name = ''
name = input('이름을 입력하세요 : ')
name

# 사용자에게 정수 2개 입력받아 더한 후 출력
#input 함수로 입력받은 데이터는 무조건 문자열로 처리됨
#만약, 숫자를 입력받길 원한다면, 적절한 변환 필요
a = input('정수를 입력하세요 :' )
b = input('정수를 입력하세요 :' )
int(a) + int(b)

#날씨 예보 프로그램
#1.입력
date = input('날짜 :')
lowestTemp = input('최저기온 :')
highestTemp = input('최고기온 :')
chanceOfRain = input('비올확률 :')
fineDust = input('미세먼지 :')
timeOfSunrise = input('일출시간 :')
timeOfSunset = input('일몰시간 :')
heightOfSouthernSea = input('남해높이 :')
heightOfEasternSea = input('동해높이 :')
heightOfWesternSea = input('서해높이 :')

print(date.split(' ')[2])

#2. 처리
weather = f'''
내일 날씨 예보입니다. 
{date.split(' ')[2]}요일인 {date[0:-2]}의 아침 최저 기온은 {lowestTemp}도, 낮 최고기온은 {highestTemp}도로 예보했습니다.
비올 확률은 {chanceOfRain}%이고, 미세먼지는 {fineDust} 수준일 것으로 예상됩니다.
일출 시간은 {timeOfSunrise}이고, 일몰 시간은 {timeOfSunset}입니다.
바다의 물결은 남해 앞바다 {heightOfSouthernSea}m, 동해 앞바다 {heightOfEasternSea}m, 서해 앞바다 {heightOfWesternSea}m 높이로 일겠습니다.
지금까지 {date}요일 날씨 예보였습니다.'''

#3. 출력
print(weather)

#2. 입력한 글자수 확인 프로그램
#메세지 입력받아 메세지의 문자길이 출력
#2-1 입력
message = input('메시지를 입력하세요 :')
#2-2 출력
print(len(message))