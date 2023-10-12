from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField()

    class Meta:
        app_label = 'personal'
