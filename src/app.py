from flask import Flask, request, send_from_directory, render_template
from flask_uploads import UploadSet, configure_uploads, ALL
import os

app = Flask(__name__)
files = UploadSet('files', ALL)
app.config['UPLOADED_FILES_DEST'] = 'uploads'
configure_uploads(app, files)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' in request.files:
        filename = files.save(request.files['file'])
        return f'File {filename} uploaded successfully'
    return 'No file uploaded', 400

@app.route('/files')
def list_files():
    file_list = os.listdir(app.config['UPLOADED_FILES_DEST'])
    return {'files': file_list}

@app.route('/files/<filename>')
def download(filename):
    return send_from_directory(app.config['UPLOADED_FILES_DEST'], filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
