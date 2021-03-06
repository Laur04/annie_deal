from django.shortcuts import render

from .models import Document

def index(request):
    return render(request, 'main/index.html')

def intro(request):
    return render(request, 'main/intro.html')

def background(request):
    docs = Document.objects.filter(page='background').order_by('date')
    return render(request, 'main/background.html', context={'docs': docs})

def alice_deal(request):
    docs = Document.objects.filter(page='miss_alice_deal').order_by('date')
    return render(request, 'main/alice_deal.html', context={'docs': docs})

def memoriam(request):
    docs = Document.objects.filter(page='alice_deal').order_by('date')
    return render(request, 'main/memoriam.html', context={'docs': docs})

def school(request):
    docs = Document.objects.filter(page='school').order_by('date')
    return render(request, 'main/school.html', context={'docs': docs})

def research(request):
    return render(request, 'main/research.html')

def document(request, doc_id):
    doc = Document.objects.get(id=doc_id)
    return render(request, 'main/document.html', context={'doc': doc})
