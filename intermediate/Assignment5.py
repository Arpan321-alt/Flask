from flask import Flask,render_template,abort
app=Flask(__name__)
@app.route('/not-found404')
def not_found():
    abort(404,"not found 404")

@app.route('/not-found500')
def not_found1():
    abort(500,"not found 505")
if __name__=='__main__':
    app.run(debug=True,port=5005)
