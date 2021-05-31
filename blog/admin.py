from django.contrib import admin
from .models import Post #modele
from .models import Bike
from .models import Accesor
# Register your models here.
admin.site.register(Post)
admin.site.register(Bike)
admin.site.register(Accesor)