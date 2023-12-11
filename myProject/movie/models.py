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
    email=models.EmailField(max_length=200,default=None, null=True)
    is_active=models.BooleanField(default=False)
    

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
    
    @classmethod
    def get_reserved_seats(cls, title, selected_theater, movie_date, running_time):
        # 해당 영화, 상영관, 예약일자, 상영시간에 대한 예약된 좌석을 가져오는 메서드
        reserved_seats = cls.objects.filter(
            title=title,
            selected_theater=selected_theater,
            movie_date=movie_date,
            running_time=running_time,
        ).values_list('selected_seat', flat=True)

        return reserved_seats
    


    def __str__(self):
        return str(self.id)


    
# Create your models here.
