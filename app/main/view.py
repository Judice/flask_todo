from . import main
from ..models import Todo, TodoForm
from flask import render_template, request


@main.route('/')
def index():
    form = TodoForm()
    todos = Todo.objects.order_by('-time')
    return render_template('index.html', todos=todos,form=form)


@main.route('/add', methods=['POST'])
def add():
    form = TodoForm(request.form)
    if form.validate():
       content = form.content.data
       todo = Todo(content=content)
       todo.save()
    todos = Todo.objects.order_by('-time')
    return render_template('index.html', todos=todos, form=form)


@main.route('/done/<string:t_id>')
def done(t_id):
    form = TodoForm()
    todo = Todo.objects.get_or_404(id=t_id)
    todo.status = 1
    todo.save()
    todos = Todo.objects.order_by('-time')
    return render_template('index.html',todos=todos,form=form)


@main.route('/undone/<string:t_id>')
def undone(t_id):
    form = TodoForm()
    todo = Todo.objects.get_or_404(id=t_id)
    todo.status = 0
    todo.save()
    todos = Todo.objects.order_by('-time')
    return render_template('index.html',todos=todos, form=form)


@main.route('/delete/<string:t_id>')
def delete(t_id):
    form = TodoForm()
    todo = Todo.objects.get_or_404(id=t_id)
    todo.delete()
    todo.save()
    todos = Todo.objects.order_by('-times')
    return render_template('index.html',todos=todos, form=form)


@main.errorhandler(404)
def not_found(e):
    return render_template('404.html'),404







