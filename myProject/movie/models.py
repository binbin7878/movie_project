from django.db import models
from django.contrib.auth.models import User
from betterforms.multiform import MultiModelForm
from django import forms

class Profile(models.Model):
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profile'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nick = models.CharField(verbose_name='NickName', max_length=50, blank=True,)
    intro = models.TextField(blank=True, max_length=200, )
    profile_image = models.ImageField(blank=True, upload_to='usr')

    def __str__(self):
        return self.nick
class MovieInfo(models.Model):
    moviename=models.CharField(max_length=20)
    movieimg=models.ImageField(blank=True, upload_to="images", null=True)
    movieopendate=models.DateField(auto_now=False, auto_now_add=False)
    moviedirector=models.CharField(max_length=20)
    mocieactor=models.CharField(max_length=20)
    moviegenre=models.CharField(max_length=20)
    movieinfo=models.CharField(max_length=30)

    def __str__(self):
        return self.moviename


    
# Create your models here.
