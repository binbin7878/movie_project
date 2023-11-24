from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.views import generic, View
from django.contrib.auth.decorators import login_required
from .forms import UserCreationMultiForm, ProfileForm
from movie.models import Profile
from django.http import JsonResponse
import requests
from bs4 import BeautifulSoup
import re
from django.core.files.base import ContentFile
from PIL import Image
from io import BytesIO
from urllib.parse import urljoin
from .models import Movieinfo
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse





# Create your views here.
def index(request):
    return render(request, 'index.html', {'title':'data'})  

def board(request):
    movies = Movieinfo.objects.all()

    return render(request, 'board.html', {'movies': movies})
def reserve(request):
    return render(request, 'reserve.html')

def mypage(request):
    return render(request,'mypage.html')



def signup(request):
    if request.method == 'POST':
        if request.POST['user-password1'] == request.POST['user-password2']:
            form = UserCreationMultiForm(request.POST, request.FILES)
            if form.is_valid(): 
                user = form['user'].save()
                profile = form['profile'].save(commit=False)
                profile.user = user
                profile.nick = user
                profile.save()
                return redirect('movie:signin')
            else:
                user = request.POST['user-username']
                user = User.objects.get(username=user)
                messages.info(request, '아이디가 중복됩니다.')
                return render(request, 'signup.html')
        else:
            messages.info(request, '비밀번호가 다릅니다.')
            return render(request, 'signup.html')
    return render(request, 'signup.html')
class Loginviews(LoginView):
    template_name = 'signin.html'

    def form_invalid(self, form):
        messages.error(self.request, '로그인에 실패하였습니다. Id 혹은 Password를 확인해 주세요.', extra_tags='danger')
        return super().form_invalid(form)

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('movie:index')
        else:
            return render(request, 'signin.html')
    else:
        return render(request, 'signin.html')


class LogoutViews(LogoutView):
    next_page = settings.LOGOUT_REDIRECT_URL

def signout(request):
    auth.logout(request)
    return redirect('movie:index')



def movielist(request):
    base_url = 'http://www.cgv.co.kr/movies/?lt=1&ft=0'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    }

    response = requests.get(base_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    movies = soup.select('#contents > div.wrap-movie-chart > div.sect-movie-chart')
    rank = []
    image = []
    title = []
    rate = []
    open_date = []
    url_number=[]

    for movie in movies:
        a_rank = movie.select('ol > li > div.box-image > strong')
        a_image = movie.select('ol > li > div.box-image > a > span > img')
        a_title = movie.select('ol> li> div.box-contents > a > strong')
        a_rate = movie.select('ol > li > div.box-contents > div > strong > span ')
        a_open_date = movie.select('ol > li > div.box-contents > span.txt-info > strong ')

    for i in range(0, len(a_rank)):
        rank.append(a_rank[i].getText())
        image.append(a_image[i]['src'])
        title.append(a_title[i].getText())
        rate.append(a_rate[i].getText())
        
        match_date = re.search(r'(\d{4}\.\d{2}\.\d{2})', a_open_date[i].getText())
        date_str = match_date.group(1).replace('.', '-') if match_date else None
        open_date.append(date_str)

        match = re.search(r'/(\d{5})/', a_image[i]['src'][::-1])  # Reversed string to match from the end
        url_number.append(match.group(1)[::-1] if match else None)

        

    movieinfo=[]
    for i in range(0,len(title)):
        movieinfo.append([rank[i],image[i],title[i],rate[i],open_date[i],url_number[i]])


    return render(request, 'movielist.html', {'movieinfo':movieinfo})

@api_view(['GET'])
def get_movies(request):
    movies = Movieinfo.objects.all()
    movie_list = []

    for movie in movies:
        movie_data = {
            'title': movie.title,
            'image_url': movie.image_url,
            'opendate': movie.opendate,
        }
        movie_list.append(movie_data)

    return Response({'movies': movie_list})


def reserve_view(request):
    if request.method == 'POST':
        # POST 데이터에서 필요한 값들을 가져옴
        title = request.POST.get('title','')
        selected_theater = request.POST.get('selectedTheater','')
        reserve_date = request.POST.get('movieDate','')
        running_time = request.POST.get('runningTime','')
        if '.' in reserve_date:
            reserve_date = reserve_date.split('.')[2]

        

        # 이후 처리를 여기에 추가

        context={
            'title':title,
            'selected_theater':selected_theater,
            'reserve_date':reserve_date,
            'running_time':running_time,
        }

        return render(request,'reserve.html',context)

       

    return render(request, 'reserve.html')


