from django.db import models
from mongoengine import *

connect('jiarui',host = '39.98.175.37',port = 27017)
# Create your models here.
class Student(Document):
    id = IntField(primary_key=True);
    name = StringField(max_length=50);
    gender = StringField(max_length=2);
    age = IntField();
    address = StringField(max_length=255);
    meta = {'jiarui':'Student'}
    def __str__(self):
        return "{id:"+str(self.id)+",name:"+self.name+"}"