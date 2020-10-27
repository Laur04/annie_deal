from django.db import models

class Document(models.Model):
    PAGES = (('background', 'Background'), ('alice_deal', 'Alice Deal'), ('school', 'School'))

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=False, null=False)
    doc_link = models.FileField(blank=False, null=False)
    
    page = models.CharField(choices=PAGES, max_length=20, blank=False, null=False)

    date = models.DateField(blank=True, null=True)
    transcript = models.TextField(max_length=10000, blank=True, null=True)
    comment = models.TextField(max_length=10000, blank=True, null=True)

    doc_pic = models.FileField(blank=True, null=True)
    doc_is_pdf = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return self.name

    @staticmethod
    def get_documents_for(page):
        return Document.objects.filter(page=page)
