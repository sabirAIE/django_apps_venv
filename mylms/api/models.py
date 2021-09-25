from django.db import models

#this imports are being used for the Signal
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# Create your models here.

class studentModel(models.Model):
    firstName       = models.CharField(max_length=50)
    lastName        = models.CharField(max_length=50)
    email           = models.CharField(max_length=100,null=False)
    createdBy       = models.CharField(max_length=100, default='unknown')
    created         = models.DateTimeField(auto_now=True)


class singerModel(models.Model):
    firstName   = models.CharField( max_length=50)
    lastName    = models.CharField(max_length=50)
    #default Values for GENDER 
    GENDER     = [
                    ('Female','Female'),
                    ('Male','Male'),
                ]
    gender      = models.CharField(choices=GENDER, max_length=50, default='')
    created     = models.DateField(auto_now=True,)

    def __str__(self):
        return self.firstName

class songModel(models.Model):
    title       = models.CharField(max_length=50)
    singer      = models.ForeignKey(singerModel, on_delete=models.CASCADE,related_name='song', null=True)
    duration    = models.IntegerField()
    created     = models.DateField(auto_now=True,)

    def __str__(self):
        return self.title


# this method or function was built to AutoGenerate Token on User Creation
@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None,created=False,*args, **kwargs):
    if created:
        # here Token is the Model for authToken in Django Rest Framework
        Token.objects.create(user=instance)