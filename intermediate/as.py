from flask import Flask, request, render_template
import os

app = Flask(__name__)

# Set the absolute path to the upload directory
UPLOAD_FOLDER = os.path.join(os.path.expanduser("~"), "desktop")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def display_page():
    return render_template('index.html')

@app.route('/upload', methods=['POST', 'GET'])
def upload_file():
    if request.method == 'POST':
        try:
            file = request.files['file']
            if file:
                filename = file.filename
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                return 'File uploaded successfully'
            else:
                return 'No file provided'
        except Exception as e:
            return str(e)
    return 'Upload a file using the provided form.'

if __name__ == '__main__':
    app.run(debug=True)