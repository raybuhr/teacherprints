from tp_app import app, db
from tp_app.models import User, Post

@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'User': User,
        'Post': Post
           }



# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database