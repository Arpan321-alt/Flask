from flask import Flask,session
app=Flask(__name__)
app.secret_key="xyz"
@app.route('/setsession')
def setSession():
    session['username']='Arpan Gupta'
    return '<h1>session has been set</h1>'
@app.route('/getsession')
def getSession():
    if 'username' in session:
        username=session['username']
        return f'Welcome {username}'
    else:
        return 'Welcome Anonymously'
@app.route('/popsession')
def popSession():
    session.pop('username')
    return 'Session popped'
if __name__=='__main__':
    app.run(host='0.0.0.0',port=8002)