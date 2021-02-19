from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from ckeditor.fields import RichTextField
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    image = models.ImageField(upload_to='blog')
    body = RichTextField(blank=False,null=False)
    # body = models.TextField()
    slug = models.SlugField(null=True, blank=True,editable=False)

    def save(self, *args, **kwargs):  
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('detail',kwargs = {'slug': self.slug})
    
    def __str__(self):
        return self.title
    
class menu(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='menu')
    price = models.IntegerField()

    def __str__(self):
        return self.title