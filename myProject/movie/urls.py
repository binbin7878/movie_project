from django.urls import path
from . import views
from .views import get_movies



app_name = 'movie'
urlpatterns = [
    path('', views.index, name='index'),

    path('board/', views.board, name='board'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='signout'),
    path('movielist/', views.movielist, name='movielist'),
    path('get_movies/', get_movies, name='get_movies'),
    path('reserve/',views.reserve_view, name='reserve'),
    path('mypage/', views.mypage, name='mypage'),
]