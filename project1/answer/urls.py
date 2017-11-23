from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout
from . import views

app_name = 'answer'
urlpatterns = [
    url(r'^(?P<question_id>[0-9]+)/create/$', views.AnswerCreate.as_view(), name='create'),
]
