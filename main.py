from flask import Flask, render_template, request, send_file, url_for, redirect
from output import Output
import os

app = Flask(__name__)
app.config['ALLOWED_EXTENSIONS'] = {'csv', 'xlsx', 'pdf', 'docx'}
app.config['UPLOAD_FOLDER'] = 'upload'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']

    if file.filename == '':
        return 'No selected file'

    if file:
        upload_folder = app.config['UPLOAD_FOLDER']
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)
        file.save(os.path.join(upload_folder, file.filename))

        output_text,output_score = Output(os.path.join(upload_folder, file.filename)).output

        return render_template('preview.html', output=[output_text,output_score])


if __name__ == "__main__":
    app.run(debug=True)
