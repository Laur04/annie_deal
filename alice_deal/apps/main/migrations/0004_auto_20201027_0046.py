# Generated by Django 3.0.6 on 2020-10-27 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_document_doc_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='doc_pic',
            field=models.FileField(blank=True, editable=False, null=True, upload_to=''),
        ),
    ]
