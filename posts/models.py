from django.db import models

# Create your models here.

class Hashtag(models.Model):
    meaning = models.TextField()
    title = models.CharField(max_length=255)



class Post(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField()
    discription = models.TextField()
    date = models.DateField()
    hashtag = models.ManyToManyField(Hashtag)
