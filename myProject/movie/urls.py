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
    path('kakaopay_success/',views.kakaopay_success,name='kakaopay_success'),
    path('kakaopay/', views.kakaopay, name='kakaopay'),
    path('check_seat_availability/<str:title>/<str:selected_theater>/<str:movie_date>/<str:running_time>/', views.check_seat_availability, name='check_seat_availability'),
    path('cancel_movie/<int:reserve_id>/', views.cancel_movie, name='cancel_movie'),
    path('check_reserve/', views.check_reserve, name='check_reserve'),

    # path('complete/', views.complete, name='complete'),
    
    
]