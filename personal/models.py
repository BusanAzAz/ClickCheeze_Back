from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(default='img/default.jpeg')

    class Meta:
        app_label = 'personal'
