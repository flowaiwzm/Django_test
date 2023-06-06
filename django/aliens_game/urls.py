from django.urls import include, path
from . import views

app_name="aliens_game"
urlpatterns = [
    # path('',include("django.contrib.auth.urls")),
    path('',views.index,name='index'),
    path('alien_invasion/', views.alien_invasion, name='alien_invasion'),
]
