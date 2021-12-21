# coding: utf-8
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
import os
import psycopg2


app = Flask(__name__)

#BDRM2
DB_HOST = "host"
DB_NAME = "name"
DB_USER = "user"
DB_PASS = "pass"




@app.route('/')
def index():
    conn = psycopg2.connect(
    host=DB_HOST,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASS,
    port="5432",
    sslmode='require')

    cursor=conn.cursor()
    cursor.execute("SELECT table_schema,table_name FROM information_schema.tables WHERE table_schema = 'public' ORDER BY table_schema,table_name")
    rows = cursor.fetchall()

    print(rows.__len__())
    if(rows.__len__()==0):
        return render_template("indexvide.html")
    else:
        cursor.execute('''SELECT * from ouvrage10''')
        data10=cursor.fetchall()
        cursor.execute('''SELECT * from ouvrage11''')
        data11=cursor.fetchall()
        cursor.execute('''SELECT * from ouvrage12''')
        data12=cursor.fetchall()
        cursor.execute('''SELECT * from ouvrage13''')
        data13=cursor.fetchall()
        cursor.execute('''SELECT * from ouvrage30''')
        data30=cursor.fetchall()
        cursor.execute('''SELECT * from ouvrage31''')
        data31=cursor.fetchall()
        cursor.execute('''SELECT * from ouvrage32''')
        data32=cursor.fetchall()
        cursor.execute('''SELECT * from ouvrage33''')
        data33=cursor.fetchall()    
        conn.close()                            
        return render_template("index.html",data10=data10,data11=data11,data12=data12,data13=data13,data30=data30,data31=data31,data32=data32,data33=data33)


if __name__ == "__main__":
    
    app.run()
    