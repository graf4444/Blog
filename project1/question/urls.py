from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout
from . import views

app_name = 'question'
urlpatterns = [
    url(r'^$', views.QuestionList.as_view(), name='question_list'),
    url(r'^(?P<pk>[0-9]+)/$', views.QuestionDetail.as_view(), name='question_detail'),
    url(r'^create/$', views.QuestionCreate.as_view(), name='question_create'),
]
