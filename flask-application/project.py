from flask import Flask,render_template,request,redirect
import MySQLdb
app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        userdetails=request.form
        name=userdetails['name']
        email=userdetails['email']
        db = MySQLdb.connect("localhost","root","Cisco@123","test" )

        cursor = db.cursor()

       # sql = """CREATE TABLE MYSQL_DB_NEW (
       # NAME  CHAR(100) NOT NULL,
       # EMAIL  CHAR(100))"""
       # cursor.execute(sql)
        sql = """INSERT INTO MYSQL_DB_NEW(NAME,
        EMAIL) VALUES (%s,%s)"""
        tuple_in=(name,email)
        cursor.execute(sql,tuple_in)


       # cursor.execute("SELECT VERSION()")
       # data = cursor.fetchone()
        db.commit()
        db.close()
        return redirect('/users')
    return render_template('index.html')
@app.route('/users')
def users():
      db = MySQLdb.connect("localhost","root","Cisco@123","test" )

      cursor = db.cursor()
      sql = """SELECT * FROM MYSQL_DB_NEW"""
      result=cursor.execute(sql)
      if result>0:
          userDetails=cursor.fetchall()
          return render_template('users.html',userDetails=userDetails)










if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
