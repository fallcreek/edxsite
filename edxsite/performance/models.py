
from mongoengine import *


class problem(Document):
    week = IntField(default=0)
    problem = IntField(default=0)
    part = IntField(default=0)


class week_problem(Document):
    set_id = StringField()
    problem_id = StringField()
    part_id = StringField()
    user_id = StringField()
    attempt = StringField()
    score = StringField()
    answer = StringField()
    timestamp = StringField()