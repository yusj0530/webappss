import MySQLdb
from django.db import models
from webappss.settings import  DATABASES

def connect():
    try:
        conn = MySQLdb.connect(
            host=DATABASES['default'][ 'HOST' ],
            port=int(DATABASES['default'][ 'PORT' ]),
            user=DATABASES['default'][ 'USER' ],
            password=DATABASES['default'][ 'PASSWORD' ],
            db=DATABASES['default'][ 'NAME' ],
            charset='utf8')
        return  conn

    except MySQLdb.Error as e:
        print('Error %d: %d' % (e.args[0], e.args[1]))
        return None

def insert(emaillist):
    try:
        conn = connect()
   # 2. 커서 생성
        cursor = conn.cursor()

    # 3. SQL문 실행
        sql = "insert into emaillist values(null, '%s', '%s', '%s')" % emaillist
        count = cursor.execute(sql)

   # 4. 자원 정리
        cursor.close()
        conn.commit()
        conn.close()

       # 5. 결과 처리
        return count == 1
    except MySQLdb.Error as e:
        print('Error %d: %d'% (e.args[0], e.args[1]))


def  fetchall():
    # 2. 커서 생성
    try:
        conn= connect()
        cursor = conn.cursor(MySQLdb.cursors.DictCursor)

        # 3. SQL문 실행
        sql = '''
            select no, first_name, last_name, email
	            from emaillist 
	            order by no desc
            '''
        cursor.execute(sql)
        # 4. 결과 받아오기(fetch)
        #  한 로우씩 넣어준다.
        results = cursor.fetchall()

        # 5. 자원 정리
        cursor.close()
        conn.close()

        return results

    except MySQLdb.Error as e:
        print('Error %d: %d' % (e.args[0], e.args[1]))
        return  None