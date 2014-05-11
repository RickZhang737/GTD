from django.conf.urls import patterns, url
from pomodoro import views

urlpatterns = patterns('',
                       url(r'^$', views.inventory, name='inventory'),
)