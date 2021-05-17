from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .models import Bike

# Create your views here.
posts = [
    {
        'author':'CoreyMS',
        'title':'Blog Post 1',
        'content':'First post content',
        'date':'2021',
    },
    {
        'author':'CoreyMS2',
        'title':'Blog Post 2',
        'content':'Second post content',
        'date':'2021',
    }
]
def home(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request,'blog/home.html',context)
def bikes(request):
    context = {		'posts':Post.objects.all(),
                    'bikes':Bike.objects.all()
	}
    return render(request,'blog/bikes.html', context)

def parts(request):
    return render(request,'blog/parts.html',{'title':'Parts'})

def accesories(request):
    return render(request,'blog/accesories.html',{'title':'Accesories'})

def rent(request):
    return render(request,'blog/rent.html',{'title':'Rent'})

def profile(request):
    return render(request,'blog/profile.html',{'title':'Profile'})

def cart(request):
    return render(request,'blog/cart.html',{'title':'Cart'})