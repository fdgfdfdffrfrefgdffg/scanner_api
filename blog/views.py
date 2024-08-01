from django.shortcuts import render
from maktab.models import Maktab
from oquvchi.models import Oquvchi

# Create your views here.
def index(request):
    maktab = Maktab.objects.all()
    return render(request, 'blog/index.html', {'maktab': maktab})

def date(request):
    return render(request, 'blog/date.html')

def sinf(request):
    oquvchi = Oquvchi.objects.all()
    return render(request, 'blog/sinf.html', {'oquvchi':oquvchi})

def oquvchi(request):
    return render(request, 'blog/oquvchi.html')

def haqida(request, id):
    haqida = Oquvchi.objects.get(id=id)
    return render(request, 'blog/haqida.html', {'haqida': haqida})

def oquvchilar(request):
    oquvchi = Oquvchi.objects.all()
    return render(request, 'blog/oquvchilar.html', {'oquvchi':oquvchi})