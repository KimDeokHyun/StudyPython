#orcle_data
#cx_oracle 설치 : pip install cx_oracle
import cx_Oracle as ora

#makedsn('호스트주소', 포트넘버, 서비스이름 = '')
dsn = ora.makedsn('localhost', 1521, service_name = 'orcl')    #오라클 접속주소

#connect(user='', password='', dsn, encoding)
conn = ora.connect(user = 'scott', password = 'tiger', dsn=dsn, encoding='UTF-8')
cur = conn.cursor()

try:
    #for row in cur.execute('SELECT * FROM emp;'):
    #    print(row)
    cur.execute('SELECT COUNT(*) FROM emp')
    result = cur.fetchone()
    print(result)
except ora.DatabaseError as e:
    print(f'쿼리문이 잘못되었습니다. 13번라인 확인요망 : {e}')
finally:
    cur.close()     #커서 닫고
    conn.close()    #접속 닫음
