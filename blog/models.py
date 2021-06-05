from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    titles = models.CharField(max_length=8)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titles

class Bike(models.Model):
    name=models.TextField()
    type=models.TextField()
    weight=models.FloatField()
    production_year=models.DateField()
    amount=models.IntegerField()
    price=models.FloatField()
    photo=models.ImageField(upload_to='bike_photo',default='bike.jpg')
    description=models.TextField()
    wheel_size=models.FloatField()
    electric=models.BooleanField(default=False)


    def __str__(self):
        return self.name

class Accesor(models.Model):
    name=models.TextField()
    production_year=models.DateField()
    amount=models.IntegerField()
    price=models.FloatField()
    photo=models.ImageField(upload_to='accessories_photo', default='default.png')
    description=models.TextField()

    def __str__(self):
        return self.name

