from bamyam.Book import Book
import bamyam.dbinfo as dbinfo

insertsql = 'insert into book(bkname, author, publisher, pubdate, retail, price, pctoff, mileage) ' \
            ' values (%s,%s,%s,%s,%s,%s,%s,%s) '
selectsql = 'select bkno, bkname, author, publisher, price from book'
selectonesql = 'select * from book where bkno = %s'
updatesql = 'update book set bkname = %s, author = %s, publisher = %s, pubdate = %s, '\
            ' retail = %s, pctoff = %s '\
            ' where bkno = %s'
deletesql = 'delete from book where bkno = %s'

class BookDAO:
    @staticmethod
    def insert_book(bk):

        cursor, conn = dbinfo.openConn()
        params = [bk.bkname, bk.author, bk.publisher, bk.pubdate,
                  bk.retail, bk.price, bk.pctoff, bk.mileage]
        cursor.execute(insertsql, params)
        conn.commit()
        rowcnt = cursor.rowcount

        dbinfo.closeConn(cursor, conn)

        return rowcnt

    @staticmethod
    def select_book():
        sql = 'select bkname, author, publisher, pubdate, price from book ' \
              ' order by sjno desc'

        cursor, conn = dbinfo.openConn()
        cursor.execute(sql)
        rows = cursor.fetchall()
        dbinfo.closeConn(cursor, conn)

        return rows

    @staticmethod
    def selectone_book():
        pass

    @staticmethod
    def update_book():
        pass

    @staticmethod
    def delete_book():
        pass











