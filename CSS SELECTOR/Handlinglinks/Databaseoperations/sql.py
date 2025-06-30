import pymysql
from requests import delete

# insert_query="insert into students values(104,'Scott',92.4)"
# update_query="update students set name='Merry_Kom'where sid=110"
delete_query="delete from students where sid=110"
try:
    connect=pymysql.connect(host="localhost",port=3306,user="root",password="Jashan@123",database="youtube")
    curs=connect.cursor()
    curs.execute(delete_query)
    connect.commit()
    curs.close()
except Exception as e:
    print(e)

