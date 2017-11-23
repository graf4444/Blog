from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from . import views

app_name = 'core'
urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^login/', LoginView.as_view(template_name = 'core/login.html'), name='login'),
    url(r'^logout/', LogoutView.as_view(), name='logout'),
    url(r'^question/', include('question.urls')),
    url(r'^anwer/', include('answer.urls')),
]
