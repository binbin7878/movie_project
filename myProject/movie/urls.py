from django.urls import path

from . import views



app_name = 'movie'
urlpatterns = [
    path('', views.index, name='index'),

    path('board/', views.board, name='board'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='signout'),
    path('movielist/', views.movielist, name='movielist')

]