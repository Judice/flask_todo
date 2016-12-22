from . import main
from ..models import Todo, TodoForm
from flask import render_template

@main.route('/')
def index():
    form = TodoForm()
    todos = Todo.objects.order_by('-time')
    return render_template('index.html', form=form, todos=todos)

