from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .models import Bike
from .models import Accesor

# Create your views here.
def home(request):
    context = {
        'posts':Post.objects.all(),
        'title': 'Home'
    }
    return render(request,'blog/home.html',context)

def bikes(request):
    context = {		'posts':Post.objects.all(),
                    'bikes':Bike.objects.all(),
                    'title':'Bikes'
	}
    return render(request,'blog/bikes.html', context)

def parts(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'Parts'
    }
    return render(request,'blog/parts.html',context)

def accesories(request):
    context = {	       'accesorieries' :Accesor.objects.all(),
                       'title': 'Accesories'
                       }
    return render(request,'blog/accesories.html',context)

def rent(request):
    context ={          'title': 'Rent'

    }
    return render(request,'blog/rent.html',context)

def profile(request):
    context ={          'title': 'Profile'

    }
    return render(request, 'blog/../templates/users/profile.html',context)

def cart(request):
    return render(request,'blog/cart.html',{'title':'Cart'})