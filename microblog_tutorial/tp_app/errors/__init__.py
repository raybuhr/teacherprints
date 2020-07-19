from flask import Blueprint

bp = Blueprint('errors', __name__)


# This `tp_app import <foo>` statement has to come at the end, after the app has
# been initialized
from tp_app.errors import handlers  # isort:skip

# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms
# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database
# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins
# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-vii-error-handling
# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xv-a-better-application-structure
# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xv-a-better-application-structure
