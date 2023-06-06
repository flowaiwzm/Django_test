"""Defines url patterns for learning_logs."""
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path,include

from . import views

urlpatterns = [
    # Home page.
    path('', views.index, name='index'),
    
    # Show all topics.
    path('topics/', views.topics, name='topics'), 
    
    # Detail page for a single topic.
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    #new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    #
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    
    # Page for editing an entry.
    path('edit_entry/<int:entry_id>/', views.edit_entry,name='edit_entry'),

    path('delete/<int:topic_id>/', views.delete_topic, name='delete_topic'),

    path('upload/', views.upload_file, name='upload'),

    path('data/',views.visualization,name='data'),

    path('weather/',views.weather_predict,name='weather'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)