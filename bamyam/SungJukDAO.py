import bamyam.dbinfo as dbinfo


class SungJukDAO:
    @staticmethod
    def insert_sungjuk(sj):
        """
        성적데이터를 sungjuk테이블에 저장
        :param sj: 성적데이터
        :return: 저장된 성적데이터 수
        """
        sql = 'insert into sungjuk(name, kor, eng, mat, tot, avg, grd) ' \
              ' values (%s,%s,%s,%s,%s,%s,%s) '

        cursor, conn = dbinfo.openConn()

        params = [sj.name, sj.kor, sj.eng, sj.mat, sj.tot, sj.avg, sj.grd]
        cursor.execute(sql, params)
        conn.commit()
        rowcnt = cursor.rowcount

        dbinfo.closeConn(cursor, conn)
        return rowcnt

    @staticmethod
    def select_sungjuk():
        """
        sungjuk테이블에서 모든 성적(번호/이름/국어/영어/수학/등록일) 데이터 가져오기
        :return: 조회된 성적데이터 객체
        """
        sql = 'select sjno, name, kor, eng, mat, regdate from sungjuk ' \
              ' order by sjno desc'

        cursor, conn = dbinfo.openConn()

        cursor.execute(sql)

        rows = cursor.fetchall()

        dbinfo.closeConn(cursor, conn)

        return rows

    @staticmethod
    def selectone_sungjuk(sjno):
        """
        sungjuk 테이블에서 특정 학생의 성적 데이터 가져오기
        :param sjno: 상세조회할 학생번호
        :return: 조회된 학생 성적 데이터
        """
        sql = ' select * from sungjuk where sjno = %s '

        cursor, conn = dbinfo.openConn()
        cursor.execute(sql, sjno)

        cursor.execute(sql, sjno)
        row = cursor.fetchone() # fetchone은 대상을 tuple객체로 만듦

        dbinfo.closeConn(cursor, conn)

        return row

    @staticmethod
    def update_sungjuk(sj, sjno):
        sql = ' update sungjuk set name=%s, kor=%s, eng=%s,' \
              ' tot=%s, avg=%s, tot=%s, grd=%s, regdate=current_timestamp ' \
              ' where sjno=%s '

        cursor, conn = dbinfo.openConn()
        params = [sj.name, sj.kor, sj.eng, sj.mat, sj.tot, sj.avg, sj.grd, sjno]
        cursor.execute(sql, params)
        conn.commit()
        rowcnt = cursor.rowcount

        dbinfo.closeConn(cursor, conn)
        return rowcnt

    @staticmethod
    def delete_sungjuk(sjno):
        """
        지정한 학생 데이터를 sungjuk테이블에서 삭제
        :param sjno: 삭제할 학생 번호
        :return: 삭제된 성적데이터 건수
        """
        sql = ' delete from sungjuk where sjno = %s '

        cursor, conn = dbinfo.openConn()

        cursor.execute(sql, sjno)
        conn.commit()
        rowcnt = cursor.rowcount

        dbinfo.closeConn(cursor, conn)

        return rowcnt


