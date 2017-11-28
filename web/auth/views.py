from django.shortcuts import render

from django.views.generic import TemplateView

# Create your views here.
class LoginView(TemplateView):
    template_name = "login.html"


def login(request, *args, **kwargs):
    div = ['<div><script type="text/javascript">/**\n* plotly.js v1....'] 

    content = [['Total number of SNR 30mm tests run: 8\n', 'Total number of passed tests: 8\n'],]
    return render(request, 'registration/login.html', {
        'div': div,
        'content': content
    })

def register(request, *args, **kwargs):
    return render(request, '')