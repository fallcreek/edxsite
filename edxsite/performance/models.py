from mongoengine import *


class problem(Document):
    week = IntField(default=0)
    problem = IntField(default=0)
    part = IntField(default=0)
