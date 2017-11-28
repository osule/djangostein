from django.conf.urls import url, include

from . import views

from auth import views as auth_views

app_name = 'home'

urlpatterns = [
    url(r'^$', views.index_secondary, name='index'),
    url(r'^photo/$', views.PhotoCreate.as_view(), name='photo'),
]