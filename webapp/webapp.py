from flask import Flask, flash, request, redirect, url_for, render_template, send_from_directory
import os
from werkzeug.utils import secure_filename

# @app.route('/uploads/<filename>')
# def uploaded_file(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'],
#                                filename)

# def shutdown_server():
#     func = request.environ.get('werkzeug.server.shutdown')
#     if func is None:
#         raise RuntimeError('Not running with the Werkzeug Server')
#     func()

# @app.route('/shutdown', methods=['POST'])
# def shutdown():
#     shutdown_server()
#     return 'Server shutting down...'



# UPLOAD_FOLDER = './audio_files'
# ALLOWED_EXTENSIONS = {'mp3',
#                       'wav',
#                       'm4a',
#                       'mp4',
#                       'aac',
#                       'asf',
#                       'flac',
#                       'xwma'
#                       }
# MAX_CONTENT_LENGTH = 16 * 1024 * 1024              # Gives 16 mb max size


# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# @app.route('upload', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         # check if the post request has the file part
#         if 'file' not in request.files:
#             flash('No file part')
#             return redirect(request.url)
#         file = request.files['file']
#         # if user does not select file, browser also
#         # submit an empty part without filename
#         if file.filename == '':
#             flash('No selected file')
#             return redirect(request.url)
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             return redirect(url_for('uploaded_file',
#                                     filename=filename))
#     return '''
#     <!doctype html>
#     <title>Upload new File</title>
#     <h1>Upload new File</h1>
#     <form method=post enctype=multipart/form-data>
#       <input type=file name=file>
#       <input type=submit value=Upload>
#     </form>
#     '''

app = Flask(__name__,
            template_folder='templates',
            static_url_path='',
            static_folder='assets')

# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH


@app.route('/')
def hello_world():
   return 'Hello, World!'
# def home():
#     return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0",
            port=80)


# https://flask.palletsprojects.com/en/1.1.x/patterns/fileuploads/