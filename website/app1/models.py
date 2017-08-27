from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
class chat(models.Model):

    fromuser = models.ForeignKey(settings.AUTH_USER_MODEL,unique=False,related_name='fromuser',on_delete=models.CASCADE,db_column='fromuser',default=1)
    touser = models.ForeignKey(settings.AUTH_USER_MODEL,unique=False,related_name='touser',on_delete=models.CASCADE,db_column='touser',default=1)
    message = models.CharField(max_length=1000,default='yeahhhh!' )

    def __str__(self):
        return self.message

class botrespond(models.Model):
    question = models.CharField(max_length=100000000,default='What?')
    answere = models.CharField(max_length=10000000,default='yes.')

    def __str__(self):
        return  self.question
