from django.conf.urls import url
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views


from . import views
from . import forms


urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$',
        auth_views.LoginView.as_view(),
        {
            'template_name': 'administration/login.html',
            'authentication_form': forms.AuthForm,
            'extra_context': {
                'next': reverse_lazy('home:index'),
            },
            'redirect_authenticated_user': True
        },
        name='login',
    ),
]
