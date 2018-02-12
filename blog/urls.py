
from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^student/$', views.portal, name='portal'),
    url(r'^student/(?P<student_id>[0-99]+)/$', views.detail, name='detail'),
    url(r'^student/add/$',views.StudentCreate.as_view(), name='student-add'),
    
    
]
