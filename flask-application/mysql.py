from flask import Flask,render_template,request
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)

@app.route('/')
def index():
    engine = create_engine('mysql://root:Cisco@123@localhost/test')
    connection = engine.connect()
    result = connection.execute("select user from mysql")
    
           
    return row['user']
           
    connection.close() 

if __name__=='__main__': 
    app.run(host='0.0.0.0',port=5000,debug=True)
