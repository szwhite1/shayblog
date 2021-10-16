from myapp import create_app, db, cli
from myapp.models import User, Post, Notification, Message, Task


app = create_app()
cli.register(app)


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Message': Message, 'Notification': Notification, 'Task': Task}