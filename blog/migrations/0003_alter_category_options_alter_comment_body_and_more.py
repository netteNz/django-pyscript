# Generated by Django 5.0.3 on 2024-08-19 04:31

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=tinymce.models.HTMLField(),
        ),
    ]
