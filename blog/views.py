from django.shortcuts import render
from maktab.models import Maktab
from oquvchi.models import Oquvchi
from django.utils import timezone

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


def kun(request):
    kunlik_malumotlar = Oquvchi.objects.filter(created_at__gte=timezone.now() - timezone.timedelta(days=1))
    jami_son = kunlik_malumotlar.count()
    return render(request, 'blog/kun.html', {'kunlik_malumotlar': kunlik_malumotlar, 'jami_son': jami_son})

def hafta(request):
    haftalik_malumotlar = Oquvchi.objects.filter(created_at__gte=timezone.now() - timezone.timedelta(days=7))
    jami_son = haftalik_malumotlar.count()
    return render(request, 'blog/hafta.html', {'haftalik_malumotlar': haftalik_malumotlar, 'jami_son': jami_son})

def oy(request):
    oylik_malumotlar = Oquvchi.objects.filter(created_at__gte=timezone.now() - timezone.timedelta(days=31))
    jami_son = oylik_malumotlar.count()

    context = {
        'oylik_malumotlar': oylik_malumotlar,
        'jami_son': jami_son
    }

    return render(request, 'blog/oy.html', context)

def yil(request):
    yillik_malumotlar = Oquvchi.objects.filter(created_at__gte=timezone.now() - timezone.timedelta(days=365))
    jami_son = yillik_malumotlar.count()

    context = {
        'yillik_malumotlar': yillik_malumotlar,
        'jami_son': jami_son
    }
    return render(request, 'blog/yil.html', context)
