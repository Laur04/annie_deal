import django
import os
import logging
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "alice_deal.settings")
django.setup()

from django.core.files.base import ContentFile

from io import BytesIO
import json
from pdf2image import convert_from_path
from pdf2image.exceptions import PDFInfoNotInstalledError, PDFPageCountError, PDFSyntaxError
from PIL import Image
import requests
from tempfile import NamedTemporaryFile

from .models import Document

for doc in Document.objects.filter(doc_is_pdf=False):
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