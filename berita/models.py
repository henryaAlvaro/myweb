from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import User


# Create your models here.

class Kategori(models.Model):
    nama = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "1. ketegori"

class Artikel(models.Model):
    judul = models.CharField(max_length=25)
    isi = models.TextField(blank=True, null=True)
    kategori = models.ForeignKey(Kategori, on_delete=models.SET_NULL, blank=True, null=True )
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    thumbnail = models.ImageField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "2. Artikel"


