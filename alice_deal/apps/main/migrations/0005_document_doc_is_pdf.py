# Generated by Django 3.0.6 on 2020-10-27 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20201027_0046'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='doc_is_pdf',
            field=models.BooleanField(default=True, editable=False),
        ),
    ]
