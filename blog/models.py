from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

class Post(models.Model):
    titles = models.CharField(max_length=16)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titles

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})

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

    def save(self):
        super().save()

        img = Image.open(self.photo.path)
        if img.height >445 or img.width >855:
            output_size = (455,855)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Accesor(models.Model):
    name=models.TextField()
    production_year=models.DateField()
    amount=models.IntegerField()
    price=models.FloatField()
    photo=models.ImageField(upload_to='accessories_photo', default='accesories.jpg')
    description=models.TextField()

    def __str__(self):
        return self.name

