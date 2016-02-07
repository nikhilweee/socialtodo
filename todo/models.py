from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Person(models.Model):
    user = models.OneToOneField(User)
    friends = models.ManyToManyField('self')

class Todo(models.Model):
    content = models.CharField(max_length=500)
    assigned_to = models.ForeignKey('Person', related_name='todos_recieved')
    assigned_by = models.ForeignKey('Person', related_name='todos_given')
    due_date = models.DateTimeField()
    date_created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
