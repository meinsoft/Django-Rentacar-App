from django.db import models
from django.utils.text import slugify
class Carlist(models.Model):
    name = models.CharField(max_length=200)
    descrpt = models.TextField()
    price = models.CharField(max_length=31, default='$31/day')
    image_url = models.URLField(max_length=200)
    benz = models.CharField(max_length=31)
    seats = models.CharField(max_length=31)
    slug = models.SlugField(null=True,unique=True,db_index=True,blank=True)
    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)
    def __str__(self):
        return self.name
