from django.db import models


# Create your models here.
# class Book(models.Model):
#    title = models.CharField()
#
# class Review(models.Model):
#    book = models.ForeignKey(Book, related_name='reviews')
#    review = models.TextField()

class Fotolar(models.Model):
    dosya = models.ImageField()
    notlar = models.TextField()
    user = models.CharField(max_length=200)
    tarih = models.DateTimeField(auto_now_add=True)
