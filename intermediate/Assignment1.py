from flask import Flask,request,render_template,send_from_directory
import os
app=Flask(__name__)
UPLOAD_FOLDER=os.path.join(os.path.expanduser("~"), "desktop")
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
@app.route('/')
def display_page():
    return render_template('index.html')

@app.route('/upload',methods=['POST'])
def upload_file():
    try:
        file=request.files['file']
        filename=file.filename
        file_location=os.path.join(app.config['UPLOAD_FOLDER'],filename)
        file.save(file_location)
        
        if filename.split('.')[1]=='txt':
            with open(file_location) as f:
                file_read=f.read()
            return render_template('content.html',text=file_read)
        elif filename.split('.')[1] in ['jpeg','png','jpg']:
            return send_from_directory(app.config['UPLOAD_FOLDER'],filename)
        return render_template('index.html')
    except Exception as e:
        return e
if __name__=='__main__':
    app.run()