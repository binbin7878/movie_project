from django.db import models
from django.contrib.auth.models import User
from betterforms.multiform import MultiModelForm
from django import forms
import MySQLdb

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
    

class Movieinfo(models.Model):
    img=models.URLField()
    title=models.CharField(max_length=50)
    opendate=models.DateField()
    image_url=models.CharField(max_length=10,primary_key=True)

    def __str__(self):
        return self.title
    
    
    @classmethod
    def create_from_crawling(cls, img, title, opendate, image_url):
        movieinfo = cls(img=img, title=title, opendate=opendate, image_url=image_url)
        movieinfo.save()
        return movieinfo

class MovieReserve(models.Model):
    id=models.AutoField(primary_key=True)
    user_id=models.ForeignKey(Profile,on_delete=models.CASCADE,default=None, null=True)
    title=models.CharField(max_length=200)
    movie_date=models.CharField(max_length=15)
    reserve_date=models.CharField(max_length=15)
    selected_seat=models.CharField(max_length=100)
    selected_theater=models.CharField(max_length=100)
    img_code=models.ForeignKey(Movieinfo,on_delete=models.CASCADE,default=None, null=True)
    payMoney=models.CharField(max_length=100,default='')
    running_time=models.CharField(max_length=10,default=None,null=True)
    
    


    def __str__(self):
        return str(self.id)


    
# Create your models here.
