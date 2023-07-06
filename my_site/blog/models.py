from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    content = models.TextField()

    def __str__(self) -> str:
        return f"{self.title}: {self.release_date} {self.content}"