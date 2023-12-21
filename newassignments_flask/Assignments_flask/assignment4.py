from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/')
def user_input():
   return  render_template("input.html")

@app.route('/input',methods=["POST"])
def display():
    first_name=request.form['fname']
    last_name=request.form['lname']

    return f'<h1>first name is {first_name} and last name is {last_name}</h1>'

if __name__=='__main__':
    app.run(host="0.0.0.0",port=8005)