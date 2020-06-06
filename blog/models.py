from django.db import models

# Create your models here.


class EditorsPick(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    author = models.CharField(max_length=50, null=True, blank=True)
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
    author = models.CharField(max_length=50, null=True, blank=True)
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


class Posts(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    author = models.CharField(max_length=50, null=True, blank=True)
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


class Newsletter(models.Model):
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.email


class CommentsTrending(models.Model):
    post = models.ForeignKey(Trending, on_delete=models.CASCADE)
    name = models.CharField(max_length=350)
    email = models.EmailField(max_length=254,null=True,blank=True)
    comment = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name


class CommentsPosts(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    name = models.CharField(max_length=350)
    email = models.EmailField(max_length=254,null=True,blank=True)
    comment = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
