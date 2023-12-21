from flask import Flask,render_template,request,redirect
import sqlite3
app=Flask('__name__')


print('table created successfully')
@app.route('/')
def display_form():
    return render_template('Student.html')
@app.route('/addRecord',methods=['POST','GET'])
def add_record():
    try:
        firstName=request.form.get('firstName')
        print(firstName)
        lastName=request.form.get('lastName')
        Class=request.form.get('class')
        totalMarks=request.form.get('totalMarks')
        conn=sqlite3.connect('student3.db')
        cur=conn.cursor()
        #cur.execute("create table students(firstname text,lastname text,class text,totalmarks text)")
        cur.execute('insert into students(firstname,lastname,class,totalmarks) values(?,?,?,?)',(firstName,lastName,Class,totalMarks))
        
        conn.commit()
        
        return  redirect('/list')
        
        # return 'data added successfully'
    except Exception as e:
        return 'method is not working properly'
@app.route('/list',methods=['POST','GET'])
def list():
        try:
            conn=sqlite3.connect('student3.db')
            cur=conn.cursor()
            conn.row_factory = sqlite3.Row
            cur.execute("select rowid,* from students")
   
            rows = cur.fetchall()
            print(rows)
            return render_template('list.html',rows=rows)
        except Exception as e:
             return 'method not working properly'
        

@app.route('/updatename.html')
def updatename():
     return render_template('updatename.html')
@app.route('/updatelastname.html')
def updatelastname():
     return render_template('updatelastname.html')
@app.route('/updateclass.html')
def updateclass():
     return render_template('updateclass.html')
@app.route('/updatetotalmarks.html')
def updatetotalmarks():
     return render_template('updatetotalmarks.html')


@app.route('/nameUpdate',methods=['POST','GET'])
def nameUpdate():
     try:
          firstname=request.form.get('firstname')
          rowid=request.form.get('rowid')
          conn=sqlite3.connect('student3.db')
          cur=conn.cursor()
          cur.execute("update students set firstname=? where rowid=? ",(firstname,rowid))
          return 'data updated successfully'
     except Exception as e:
          print(e)
          return 'data not proper handling'
     
@app.route('/Class',methods=['POST','GET'])
def Class():
     try:
        Class=request.form.get('Class')
        rowid=request.form.get('rowid')
        conn=sqlite3.connect('student3.db')
        cur=conn.cursor()
        cur.execute('update students set class=? where rowid=?',(Class,rowid))
        return 'data update successfully'
     except Exception as e:
          print(e)
          return 'Something Wrong'
@app.route('/lastNameUpdate',methods=['POST','GET'])
def lastnameupdate():
     try:
        lastname=request.form.get('lastname')
        rowid=request.form.get('rowid')
        conn=sqlite3.connect('student3.db')
        cur=conn.cursor()
        cur.execute('update students set lastname=? where rowid=?',(lastname,rowid))
        return 'data update successfully'
     except Exception as e:
          print(e)
          return 'Something Wrong'
@app.route('/UpdateTotalMarks',methods=['POST','GET'])
def totalmarksupdate():
     try:
        totalmarks=request.form.get('totalmarks')
        rowid=request.form.get('rowid')
        conn=sqlite3.connect('student3.db')
        cur=conn.cursor()
        cur.execute('update students set totalmarks=? where rowid=?',(totalmarks,rowid))
        return 'data update successfully'
     except Exception as e:
          print(e)
          return 'Something Wrong'

@app.route('/deleteRecord',methods=['POST','GET'])
def deleteRecord():
     rowid=request.form.get('rowid')
     conn=sqlite3.connect('student3.db')
     cur=conn.cursor()
     cur.execute('delete from students where rowid=?',rowid)
     conn.close()
     return 'data deleted successfully'
@app.route('/fetchRecord',methods=['POST','GET'])
def fetchRecord():
    conn=sqlite3.connect('student3.db')
    cur=conn.cursor()
    cur.execute('select rowid,* from students')
    rows=cur.fetchall()
    return render_template('list.html',rows=rows)
if __name__=='__main__':
    app.run()