import sys
from collections import OrderedDict
# import oracledb
import pymysql

# 데이터베이스 연결정보
url = '2.rds.amazonaws.com'
userid = ''
passwd = ''
dbname = 'bigdata'




# 메뉴 출력
def show_menu():
    """
    메뉴 출력하기
    :return:
    """
    main_menu = '''
--------------------
성적처리 프로그램 v7
--------------------
1. 성적 데이터 추가
2. 성적 데이터 조회
3. 성적 데이터 상세조회
4. 성적 데이터 수정
5. 성적 데이터 삭제
0. 프로그램 종료
--------------------
'''
    print(main_menu)
    menu = input("=> 메뉴를 선택하세요 : ")
    return menu

# 성적 데이터 입력받음
def read_sungjuk():
    """
    이름과 성적 데이터(국어, 영어 수학)를
    dict형 변수인 user에 기입
    :return: user(name, kor, eng, mat)
    """
    sungjuk = input('이름과 성적을 입력하세요(예 : 홍길동 99 88 99) :')
    data = sungjuk.split() # 빈칸을 문자열로 분리할 때는 구분자를 안 넣으면 빈칸으로 인식

    name = data[0]
    kor = int(data[1])
    eng = int(data[2])
    mat = int(data[3])
    sj = [name, kor, eng, mat] # 입력받은 성적 데이터를 리스트에 담음
    return sj

# 성적 처리(총점/평균/학점 계산)
def compute_sungjuk(sj):
    """
    성적 처리(총점/평균/학점 계산)
    user에 담긴 성적 데이터를 처리하는 프로그램
    :param user: read_sungjuk에서 만든 성적데이터
    :return: 성적처리된 성적데이터
    """
    tot = sj[1] + sj[2] + sj[3]
    avg = float(f"{tot/3:.1f}")
    grd = '수' if avg >= 90 else \
        '우' if avg >= 80 else \
            '미' if avg >= 70 else \
                '양' if avg >= 60 else '가'

    return [sj[0], sj[1], sj[2], sj[3], tot, avg, grd]

# 성적 데이터 저장(sungjuk 테이블)
def save_sungjuk(sj):  # 이제는 파일과 메모리의 sjs변수에 값을 저장
    # 메모리 내에 생성된 json객체에 방금 생성한 성적 데이터 저장
    """
    성적 데이터 저장(sungjuk 테이블)
    :param sj: user(name, kor, eng, mat, tot, avg, grd)
    :return: 없음
    """
    sql = 'insert into sungjuk(name, kor, eng, mat, tot, avg, grd) '\
        " values (%s,%s,%s,%s,%s,%s,%s) "
        # " values (:1,:2,:3,:4,:5,:6,:7) "
    # ' values (:name,:kor,:eng,:mat,:tot,:avg,:grd)'
          # ' values (?, ?, ?, ?, ?, ?, ?)'
        # ' values (?,?,?,?,?,?,?)' 오라클에서는 불가능

    conn = pymysql.connect(host=url, user=userid, password= passwd, database= dbname, charset='utf8')

    cursor = conn.cursor()

    cursor.execute(sql, sj)
    conn.commit()
    print(cursor.rowcount, '건의 성적데이터 추가됨!')

    cursor.close()
    conn.close()

# 성적 데이터 추가(입력 -> 처리 -> 저장)
def add_sungjuk():
    """
    성적 데이터 추가(입력 -> 처리 -> 저장)\n
    입력함수에서 데이터를 user에 받고, 처리함수에서 데이터를 user에 더 추가하고
    저장함수에서 user를 받아 저장함
    :return:
    """
    print('성적데이터 추가')
    sj = read_sungjuk()
    sj = compute_sungjuk(sj)
    save_sungjuk(sj)

# 모든 학생의 일부분의 성적 데이터 출력(번호/이름/국어/영어/수학/등록일)
def show_sungjuk():
    """
    모든 학생의 일부분의 성적 데이터 출력(이름/국어/영어/수학)
    :return:
    """
    sql = 'select sjno, name, kor, eng, mat, regdate from sungjuk '\
            ' order by sjno desc'
    # conn = oracledb.connect(
    #     user=user, password=passwd, dsn=dsn_tsn)
    conn = pymysql.connect(host=url, user=userid, password= passwd, database= dbname, charset='utf8')

    cursor = conn.cursor()

    cursor.execute(sql)

    for sjno, name, kor, eng, mat, regdate in cursor:
        print(sjno, name, kor, eng, mat, str(regdate)[:10])

    cursor.close()
    conn.close()


# 특정 학생의 모든 성적 데이터 출력
def showone_sungjuk():
    """
    특정 학생의 모든 성적 데이터 출력
    :return:
    """
    print('성적데이터 상세조회')
    sjno = input('상세 조회할 학생번호는?')

    sql = ' select * from sungjuk where sjno = %s '

    conn = pymysql.connect(host=url, user=userid, password= passwd, database= dbname, charset='utf8')

    cursor = conn.cursor()

    cursor.execute(sql, [sjno])

    for sjno, name, kor, eng, mat, tot, avg, grd, regdate in cursor:
        print(sjno, name, kor, eng, mat, tot, avg, grd, str(regdate)[:10])

    cursor.close()
    conn.close()


    info = '찾는 데이터가 없습니다'


    print(info)

# 성적 수정 시 이름을 통해 성적을 변수에 저장
def read_again(sjno):
    """
    성적 데이터 수정 시 수정할 데이터 입력받는 함수
    :param sjno: 수정할 학생번호
    :return: 새롭게 수정된 성적데이터
    """
    sql = ' select name, kor, eng, mat from sungjuk where sjno = %s '
    conn = pymysql.connect(host=url, user=userid, password= passwd, database= dbname, charset='utf8')
    cursor = conn.cursor()
    cursor.execute(sql, [sjno])

    sj = [None, None, None, None]
    for name, kor, eng, mat in cursor:
        sj = [name, kor, eng, mat]

    cursor.close()
    conn.close()

    if sj[0]: # 만일 수정할 데이터가 존재한다면
        sj[0] = input(f'새로운 이름은? ({sj[0]}) : ')
        sj[1] = int(input(f"새로운 국어는? ({sj[1]})"))
        sj[2] = int(input(f"새로운 영어는? ({sj[2]})"))
        sj[3] = int(input(f"새로운 수학은? ({sj[3]})"))
        sj = compute_sungjuk(sj)
    return sj



# 성적 데이터 수정/삭제 시 변경사항을 파일에 반영

#  성적 데이터 수정
def modify_sungjuk():
    """
    성적 데이터 수정
    :return: 없음
    """
    print('성적데이터 수정')
    sjno = input('수정할 학생 번호는?')

    sj = read_again(sjno)

    if sj[0]:
        sql = ' update sungjuk set name=%s, kor=%s, eng=%s,'\
              ' tot=%s, avg=%s, tot=%s, grd=%s, regdate=current_timestamp '\
              ' where sjno=%s '
        sj.append(sjno)
        conn = pymysql.connect(host=url, user=userid, password= passwd, database= dbname, charset='utf8')
        cursor = conn.cursor()
        cursor.execute(sql, sj)
        conn.commit()
        print(f'{cursor.rowcount} 건의 데이터가 수정되었습니다')
        cursor.close()
        conn.close()

    else:
        print('찾는 데이터가 없습니다!')


# 성적 데이터 삭제
def remove_sungjuk():
    """
    성적 데이터 삭제
    :param 없음:
    :return: 없음
    """
    print('성적데이터 제거')
    sjno = input('삭제할 학생번호는?')
    sql = ' delete from sungjuk where sjno = %s '
    # 삭제할 데이터 찾기

    conn = pymysql.connect(host=url, user=userid, password= passwd, database= dbname, charset='utf8')
    cursor = conn.cursor()

    cursor.execute(sql, [sjno])
    conn.commit()
    print(f'{cursor.rowcount} 건의 데이터가 삭제되었습니다')

    cursor.close()
    conn.close()


# 프로그램 종료
def exit_program():
    """
    sungjuk program exit
    :return: None
    """
    print('프로그램을 종료합니다')
    sys.exit(0)