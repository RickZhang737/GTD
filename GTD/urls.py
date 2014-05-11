from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'GTD.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^polls/', include('polls.urls', namespace='polls')),
                       url(r'^pomodoro/', include('pomodoro.urls', namespace='pomodoro')),
                       url(r'^$', 'GTD.hello.index'),
                       url(r'^admin/', include(admin.site.urls)),
)
