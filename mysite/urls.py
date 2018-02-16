
from django.conf.urls import include, url
from django.contrib import admin
from blog import views
from django.contrib import admin
from django.contrib.auth import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls')),
    url(r'^login/$', views.login, name='login'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    
]
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'home'
