# Generated by Django 3.1.1 on 2020-11-24 20:54

import autoslug.fields
from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0004_auto_20201124_1840'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='created',
            field=model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created'),
        ),
        migrations.AddField(
            model_name='band',
            name='modified',
            field=model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified'),
        ),
        migrations.AddField(
            model_name='band',
            name='profile',
            field=models.TextField(blank=True, verbose_name='Profile'),
        ),
        migrations.AddField(
            model_name='band',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=django.utils.timezone.now, editable=False, populate_from='name', unique=True, verbose_name='Band Address'),
            preserve_default=False,
        ),
    ]