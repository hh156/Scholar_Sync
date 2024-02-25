
from django.urls import path
from . import views
app_name = 'homepage'
urlpatterns = [
# post views
    path('', views.home),
    path('leaderboard/', views.leaderboard),
    path('apcsa/', views.apcsa),
    path('bio/', views.bio),
    path('<int:id>/', views.post_detail, name='post_detail'),
]