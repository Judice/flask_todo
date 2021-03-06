# coding=utf-8
from app import db
from flask_mongoengine.wtf import model_form
import datetime


class Todo(db.Document):
    content = db.StringField(required=True, max_length=20)
    time = db.DateTimeField(default=datetime.datetime.now())
    status = db.IntField(default=0)

TodoForm = model_form(Todo) # 进行表单验证