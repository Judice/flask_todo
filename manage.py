# conding=utf-8
from flask_script import Manager, Server
from app.models import Todo
from app import create_app
import os

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

manager.add_command("runserver",
                    Server(host='0.0.0.0',
                           port=5000,
                           use_debugger=True))


@manager.command
def save_todo():
    todo = Todo(content="my first todo")
    todo.save()


if __name__ == '__main__':
    manager.run()