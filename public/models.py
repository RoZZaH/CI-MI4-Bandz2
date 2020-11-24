from django.db import models
from .sqlite_listfield import ListField

# Create your models here.
class County(models.Model):
    name = models.CharField("County", max_length=55)
    friendly_name = models.CharField(max_length=55, null=True, blank=True)

    class Province(models.TextChoices):
        ULSTER = "ulster", "Ulster"
        LEINSTER = "leinster", "Leinster"
        MUNSTER = "munster", "Munster"
        CONNACHT = "connacht", "Connacht"

    province = models.CharField("Province", max_length=10, choices=Province.choices, default=Province.LEINSTER)
    towns = ListField(null=False)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name
