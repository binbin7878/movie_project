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


# Create your views here.
def index(request):
    return render(request, 'index.html', {'title':'data'})  

def board(request):
    return render(request, 'board.html', {'title':'board'})



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
    url = 'http://www.cgv.co.kr/movies/?lt=1&ft=0'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    movies = soup.select('#contents > div.wrap-movie-chart > div.sect-movie-chart')
    rank = []
    image = []
    title = []
    rate = []
    open_date = []

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
        open_date.append(a_open_date[i].getText().replace('\r\n', '').strip().replace('\n', '').replace(' ', ''))

    movieinfo=[]
    for i in range(0,len(title)):
        movieinfo.append([rank[i],image[i],title[i],rate[i],open_date[i]])


    return render(request, 'movielist.html', {'movieinfo':movieinfo})


    

