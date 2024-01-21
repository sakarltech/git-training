from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # Assuming your S3 bucket name is 'your-s3-bucket'
        upload_to_s3(os.path.join(app.config['UPLOAD_FOLDER'], filename), 'your-s3-bucket', filename)
        return 'File Uploaded Successfully'

    return 'Invalid File'

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    # Assuming your S3 bucket name is 'your-s3-bucket'
    download_from_s3('your-s3-bucket', filename, os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
