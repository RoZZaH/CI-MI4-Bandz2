from enum import unique
from django.contrib.postgres.fields import ArrayField, CICharField
# from .sqlite_listfield import ListField
from django.db.models.fields import CharField
from autoslug import AutoSlugField
from django.db import models
from model_utils.models import TimeStampedModel

from bandz2.utils.helpers import *

# Create your models here.
class County(models.Model):

    class Meta:
        verbose_name_plural = 'Counties'

    name = models.CharField("County", max_length=12)
    friendly_name = models.CharField(max_length=20, null=True, blank=True)

    class Province(models.TextChoices):
        ULSTER = "ulster", "Ulster"
        LEINSTER = "leinster", "Leinster"
        MUNSTER = "munster", "Munster"
        CONNACHT = "connacht", "Connacht"

    province = models.CharField("Province", max_length=10, choices=Province.choices, default=Province.LEINSTER)
    towns = ArrayField(models.CharField(max_length=64))

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Band(TimeStampedModel):
    # data_created default now
    name = CICharField("Band / Artist Name", max_length=64)
    catalogue_name = CICharField(max_length=72, blank=True)
    slug = AutoSlugField("Band Address", unique=True, always_update=False, populate_from="name")
    profile = models.TextField("Profile", blank=True)
    #hometown = 
    homecounty = models.ForeignKey('County', null=False, blank=False, on_delete=models.DO_NOTHING)

    #category

    def save(self, *args, **kwargs):
        self.catalogue_name = de_article(self.name)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name
