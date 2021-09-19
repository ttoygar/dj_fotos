from django.db import models


# def user_directory_path(instance, filename):
#     # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
#     return 'user_{0}/{1}'.format(instance.user.id, filename)

class Fotolar(models.Model):
    # dosya = models.ImageField(upload_to=user_directory_path)
    dosya = models.ImageField(upload_to='dosyalar/')
    notlar = models.TextField()
    user = models.CharField(max_length=200)
    tarih = models.DateTimeField(auto_now_add=True)
