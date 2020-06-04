from django.db import models

# Create your models here.


class EditorsPick(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    tag = models.CharField(max_length=50)
    date_Created = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='Editors_pick')

    def __str__(self):
        return self.title

    @property
    def imageUrl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
