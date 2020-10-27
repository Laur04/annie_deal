from django.core.files.base import ContentFile
from django.shortcuts import render

from io import BytesIO
import json
from pdf2image import convert_from_path
from pdf2image.exceptions import PDFInfoNotInstalledError, PDFPageCountError, PDFSyntaxError
from PIL import Image
import requests
from tempfile import NamedTemporaryFile

from .models import Document

def index(request):
    return render(request, 'main/index.html')

def background(request):
    docs = [[d, get_img(d)] for d in Document.get_documents_for('background').order_by('date')]
    return render(request, 'main/background.html', context={'docs': docs})

def alice_deal(request):
    docs = [[d, get_img(d)] for d in Document.get_documents_for('alice_deal').order_by('date')]
    return render(request, 'main/alice_deal.html', context={'docs': docs})

def school(request):
    docs = [[d, get_img(d)] for d in Document.get_documents_for('school').order_by('date')]
    return render(request, 'main/school.html', context={'docs': docs})

def document(request, doc_id):
    doc = Document.objects.get(id=doc_id)
    return render(request, 'main/document.html', context={'doc': doc})

def get_img(doc):
    with NamedTemporaryFile() as tf:
        r = requests.get(doc.doc_link.url, stream=True)
        for chunk in r.iter_content(chunk_size=4096):
            tf.write(chunk)
        tf.seek(0)
        new_image = convert_from_path(tf.name)[0]

        new_image_io = BytesIO()
        new_image.save(new_image_io, format='PNG')

        doc.doc_pic.save(
            str(doc.id) + '.png',
            content=ContentFile(new_image_io.getvalue()),
            save=False
        )
        doc.doc_is_pdf = True
        doc.save()

# def get_img(doc):
#     if doc.doc_is_pdf is None:
#         try:
#             with NamedTemporaryFile() as tf:
#                 r = requests.get(doc.doc_link.url, stream=True)
#                 for chunk in r.iter_content(chunk_size=4096):
#                     tf.write(chunk)
#                 tf.seek(0)
#                 new_image = convert_from_path(tf.name)[0]

#                 new_image_io = BytesIO()
#                 new_image.save(new_image_io, format='PNG')

#                 doc.doc_pic.save(
#                     str(doc.id) + '.png',
#                     content=ContentFile(new_image_io.getvalue()),
#                     save=False
#                 )
#                 doc.doc_is_pdf = True
#                 doc.save()
#         except:
#             doc.doc_is_pdf = False
#             doc.save()
#     return doc.doc_is_pdf
