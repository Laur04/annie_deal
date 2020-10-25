from django.shortcuts import render
from django.core.files import File
from os.path import basename
import requests
from tempfile import TemporaryFile
from urllib.parse import urlsplit

from .models import Document

def index(request):
    return render(request, 'main/index.html')

def background(request):
    docs = Document.get_documents_for('background').order_by('date')
    return render(request, 'main/background.html', context={'docs': docs})

def alice_deal(request):
    docs = Document.get_documents_for('alice_deal').order_by('date')
    return render(request, 'main/alice_deal.html', context={'docs': docs})

def school(request):
    docs = Document.get_documents_for('school').order_by('date')
    return render(request, 'main/school.html', context={'docs': docs})

def document(request, doc_id):
    doc = Document.objects.get(id=doc_id)
    return render(request, 'main/document.html', context={'doc': doc})
