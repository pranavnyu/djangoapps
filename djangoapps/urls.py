from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    url(r'^quiz/', include('quiz.urls', namespace="quiz")),
    #url(r'^(?P<question_id>\d+)/score/$', views.score, name='score'),
    url(r'^admin/', include(admin.site.urls)),
)
