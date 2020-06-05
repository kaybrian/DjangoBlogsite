from django.db import models

# Create your models here.


class EditorsPick(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    author = models.CharField(max_length=50,null=True,blank=True)
    tag = models.CharField(max_length=50)
    date_Created = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='Editors_pick')

    def __str__(self):
        return self.title
    @property
    def authorPrest(self):
        try:
            post = self.author
        except:
            post = ''
        return post

    @property
    def imageUrl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url




class Trending(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    author = models.CharField(max_length=50,null=True,blank=True)
    tag = models.CharField(max_length=50)
    date_Created = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='Trends')
   

    def __str__(self):
        return self.title
    @property
    def authorPrest(self):
        try:
            post = self.author
        except:
            post = ''
        return post

    @property
    def imageUrl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class TrendingBig(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    author = models.CharField(max_length=50,null=True,blank=True)
    tag = models.CharField(max_length=50)
    date_Created = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='Trends')
   

    def __str__(self):
        return self.title
    @property
    def authorPrest(self):
        try:
            post = self.author
        except:
            post = ''
        return post

    @property
    def imageUrl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
