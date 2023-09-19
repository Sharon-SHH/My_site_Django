from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    content = models.TextField()
    slug = models.SlugField(default="", null=False)

    def __str__(self) -> str:
        return f"{self.title}: {self.release_date} {self.content}"
    
    def get_absolute_url(self):
        return reverse("blog-detail", args=[self.slug]) # add this function to link
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    