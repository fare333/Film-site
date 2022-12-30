from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Film(models.Model):
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos/')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    description = models.TextField()
    year = models.IntegerField()
    actors = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    language = models.CharField(max_length=50)
    duration = models.IntegerField()
    rating = models.IntegerField()
    trending = models.BooleanField()
    popular = models.BooleanField()
    image = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.title
    

    