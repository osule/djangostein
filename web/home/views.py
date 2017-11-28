from django.shortcuts import render, reverse
from django.http import JsonResponse
from django.views.generic.edit import CreateView
# Create your views here.


from .models import Photo

from utils import add


class PhotoCreate(CreateView):
    model = Photo

    fields = ['img',] 

    def get_success_url(self):
        return reverse('home:index')

def index(request):
    total = add(1,2,3,4)
    return JsonResponse({'total': total})

def index_secondary(request):
    photos = Photo.objects.all()
    return render(request, 'index.html', {'photos': photos})

def register(request):
    return JsonResponse({'page': 'register'})
