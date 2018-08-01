from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1024)
    category = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    created = models.DateTimeField('Date Created')
    modified = models.DateTimeField('Date modified')

    def __str__(self):
        return self.title