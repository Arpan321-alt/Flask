from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def get_url():
    name=request.args.get('name')
    age=request.args.get('age')

    return f'name is {name} and age is {age}'
if __name__=='__main__':
    app.run('0.0.0.0',port=8002)