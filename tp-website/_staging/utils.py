from flask import request
from default_config import ALLOWED_EXTENSIONS


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def create_app(app_name='TEACHERPRINTS'):
    app = Flask(app_name)
    app.config.from_object('webapp.default_config')
    app.config.from_envvar('TEACHERPRINTS_SETTINGS')
    # from api.api import api
    # app.register_blueprint(api, url_prefix='/api')
    # from api.models import db
    # db.init_app(app)
    return app