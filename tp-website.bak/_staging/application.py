from flask import Flask, flash, request, redirect, url_for, render_template, send_from_directory
import os
from werkzeug.utils import secure_filename
from teacherprints-ui.webapp import utils


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'


@app.route('upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

app = Flask(__name__,
            template_folder='templates',
            static_url_path='',
            static_folder='assets')

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0",
            port=80)


def create_app(app_name='TEACHERPRINTS'):
    app = Flask(app_name)
    app.config.from_object('webapp.default_config')
    app.config.from_envvar('TEACHERPRINTS_SETTINGS')
    # from api.api import api
    # app.register_blueprint(api, url_prefix='/api')
    # from api.models import db
    # db.init_app(app)
    return app

# References
# https://flask.palletsprojects.com/en/1.1.x/config/
# https://flask.palletsprojects.com/en/1.1.x/patterns/fileuploads/
