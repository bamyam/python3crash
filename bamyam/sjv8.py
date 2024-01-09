import sys
from collections import OrderedDict
# import oracledb
import pymysql
from bamyam.SungJuk import SungJuk
from bamyam.SungJukService import SungJukService
from bamyam.SungJukDAO import SungJukDAO



# 메뉴 출력
def show_menu():
    """
    메뉴 출력하기
    :return:
    """
    main_menu = '''
--------------------
성적처리 프로그램 v8
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

# 성적 데이터 추가(입력 -> 처리 -> 저장)
def add_sungjuk():
    """
    성적 데이터 추가(입력 -> 처리 -> 저장)\n
    입력함수에서 데이터를 user에 받고, 처리함수에서 데이터를 user에 더 추가하고
    저장함수에서 user를 받아 저장함
    :return:
    """
    print('성적데이터 추가')
    sj = SungJukService.read_sungjuk()
    SungJukService.compute_sungjuk(sj)
    rowcnt = SungJukDAO.insert_sungjuk(sj)
    print(f'{rowcnt} 건의 성적이 추가되었습니다')

# 성적 데이터 저장(sungjuk 테이블)


def show_sungjuk():
    """
    모든 학생의 일부분의 성적 데이터 출력(이름/국어/영어/수학)
    :return:
    """
    rows = SungJukDAO.select_sungjuk()
    for row in rows:
        print(f'학번 : {row[0]:}, 이름 : {row[1]}, 국어 : {row[2]:2d}, 영어 : {row[3]:2d}, '
              f'수학 : {row[4]:2d}, 등록일 :{str(row[5])[:10]}')

# 특정 학생의 모든 성적 데이터 출력
def showone_sungjuk():
    """
    특정 학생의 모든 성적 데이터 출력
    :return:
    """
    print('성적데이터 상세조회')
    sjno = input('상세 조회할 학생번호는?')
    row = SungJukDAO.selectone_sungjuk(sjno)

    print(f'학번 : {row[0]:}, 이름 : {row[1]}, 국어 : {row[2]:2d}, 영어 : {row[3]:2d}, '
          f'수학 : {row[4]:2d}, 총점 : {row[5]}, 평균 : {row[6]}, 학점 : {row[7]}, 등록일 :{str(row[8])[:10]}')

# 성적 데이터 수정/삭제 시 변경사항을 파일에 반영
#  성적 데이터 수정
def modify_sungjuk():
    """
    성적 데이터 수정
    :return: 없음
    """
    print('성적데이터 수정')
    sjno = input('수정할 학생 번호는?')

    sj = list(SungJukDAO.selectone_sungjuk(sjno)) # 튜플로 넘어온 객체를 list로 변환

    if sj[0]: # 만일 수정할 데이터가 존재한다면
        sj[1] = input(f'새로운 이름은? ({sj[1]}) : ')
        sj[2] = int(input(f"새로운 국어는? ({sj[2]})"))
        sj[3] = int(input(f"새로운 영어는? ({sj[3]})"))
        sj[4] = int(input(f"새로운 수학은? ({sj[4]})"))
        # 조회한 결과를 클래스타입으로 변경 후 다시 성적처리
        sj = SungJuk(sj[1], sj[2], sj[3], sj[4])
        SungJukService.compute_sungjuk(sj)

        rowcnt = SungJukDAO.update_sungjuk(sj, sjno)
        print(f'{rowcnt} 건의 데이터가 수정되었습니다')

    else :
        print('데이터가 존재하지 않습니다')


# 성적 데이터 삭제
def remove_sungjuk():
    """
    성적 데이터 삭제
    :param 없음:
    :return: 없음
    """
    print('성적데이터 제거')
    sjno = input('삭제할 학생번호는?')
    rowcnt = SungJukDAO.delete_sungjuk(sjno)

    print(f'{rowcnt} 건의 데이터가 삭제되었습니다')

# 프로그램 종료
def exit_program():
    """
    sungjuk program exit
    :return: None
    """
    print('프로그램을 종료합니다')
    sys.exit(0)