from django.contrib import admin
from django.urls import path
from . import views


app_name = 'home'
urlpatterns = [
    path('',  views.HomeView.as_view() , name='home'),
    path('send-message/', views.SendMessageView.as_view(), name='send_message'),
    path('save-document/', views.SaveDocumentView.as_view(), name='save_document'),
]
