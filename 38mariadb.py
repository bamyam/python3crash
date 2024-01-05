# 마리아디비로 데이터 다루기 1 - select
# pymysql 모듈을 먼저 설치해야 함 - pip install pymysql

import pymysql

# 데이터베이스 서버 접속정보 정의(로컬에서만 구동)
url = 'ap-northeast-2.rds.amazonaws.com'
userid = ''
passwd = ''
dbname = 'bigdata'

# 디비 서버에 연결
conn = pymysql.connect(host=url, user=userid, password= passwd, database= dbname, charset='utf8')

cursor = conn.cursor()
sql = 'select * from member '
cursor.execute(sql)

# 반복문으로 하나씩 꺼내와서 데이터베이스와의 연결을
rows = cursor.fetchall() # sql 실행결과를 결과집합으로 모두 가져옴

cursor.close()
conn.close()

result = ''
for row in rows:
    result += f'{row[0]}, {row[1]}, {row[2]}, {row[3]} \n'

print(result)

# 승선위치별(embark_town) 성별(sex) 생존자수(alive) 조회

