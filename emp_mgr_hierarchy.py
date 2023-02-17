import mysql.connector
    
# response
mydb = mysql.connector.connect(
    host="localhost",
      user="root",
      password="babu",
      database='el'
    )

mycursor = mydb.cursor(dictionary=True)

mycursor.execute(""" WITH RECURSIVE category_path (employee_id, last_name,manager_id,path , lvl) AS
(
  SELECT employee_id,last_name, manager_id, CAST(concat(last_name,'( ',job_id ,' )') AS CHAR(100)) as path ,0 AS lvl
    FROM employees
    WHERE manager_id=0
  UNION ALL
  SELECT c.employee_id,c.last_name,c.manager_id, CONCAT(cp.path, ' --> ', concat(c.last_name,'( ',job_id ,' )')),lvl+1 AS lvl
    FROM category_path AS cp JOIN employees AS c
      ON cp.employee_id = c.manager_id
)

SELECT last_name,path,lvl FROM category_path
ORDER BY path""")

myresult = mycursor.fetchall()


AA = '│'

BB = '└──'
CC = '├──'

DD = '│   '
EE = '    '

for x in myresult:
  a = x.get('lvl')
  if a ==0:
    print(AA*a,x.get('last_name'),x.get('lvl'))
  elif a==1:
    print(EE*a,BB,x.get('last_name'),x.get('lvl'))
  elif a==2:
    print(EE*a,BB,x.get('last_name'),x.get('lvl'))
  else:
    print(EE*a,BB,x.get('last_name'),x.get('lvl'))

#a = x.get('last_name')
#print(a)
  

  #print('|_>'*
  
print(mydb)
