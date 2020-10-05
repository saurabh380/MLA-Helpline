from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class extenduser(models.Model):
    firname=models.TextField(max_length=15)
    fname=models.TextField(max_length=15)
    gnpan=models.TextField(max_length=20)
    gramp = models.TextField(max_length=20)
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='euser')

class complaindata(models.Model):
    department = models.CharField(max_length=30)
    gram_nagar = models.CharField(max_length=30)
    com_subject = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    upload_file = models.FileField(blank=True,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    status=models.CharField(max_length=100,default="Recieved")





