# path : testdb\\test_oracle2.py
# 오라클 연동과 insert 쿼리문 실행 테스트

# 1.
import cx_Oracle
import os
import common.dbConnectTemplate as dbtemp

# 2.
dbtemp.oracle_init()
conn = dbtemp.connect()

# 3.
# query = "insert into member values('user77', 'pass77', '파이선', 'M', 33, '010-9999-2222', 'python@python.com', default, default, default, default, default, null)"

# insert 구문에 사용할 값을 외부 데이터를 이용할 경우 (키보드 입력 데이터 등)
# 주의 : 쿼리문에 적용할 외부 값은 반드시 튜플로 저장해야 함
# 키보드로 값을 입력받아서 튜플에 저장 처리 :
data = (input('아이디:  '),
            input('패스워드: '),
            input('이름: '),
            input('성별: '),
            int(input('나이: ')),
            input('전화번호: '),
            input('e-mail: '))


# 튜플을 쿼리문에 적용할 떄, 값을 1234 순으로 적용해야 함(순서 주의)
query = "insert into member values(:1, :2, :3, :4, :5, :6, :7, default, default, default, default, default, null)"

# 4.
cursor = conn.cursor()

try:
    cursor.execute(query, data)
    conn.commit()
except:
    conn.rollback()
finally:
    cursor.close()
    dbtemp.close(conn)


