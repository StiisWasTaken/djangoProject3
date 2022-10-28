from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .models import Bike
from .models import Accesor
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView, DetailView, CreateView, UpdateView,DeleteView)

# Create your views here.
def home(request):
    context = {
        'posts':Post.objects.all(),
        'title': 'Home'
    }
    return render(request,'blog/home.html',context)

class WpisLista(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class WpisSzczegoly(DetailView):
    model = Post

class WpisTworzenie(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['titles','content']

    def form_valid(self, form):
        form.instance.author =self.request.user
        return super().form_valid(form)

class WpisAktualizacja(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['titles','content']

    def form_valid(self, form):
        form.instance.author =self.request.user
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

class WpisUsun(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

def bikes(request):
    context = {		'posts':Post.objects.all(),
                    'bikes':Bike.objects.all(),
                    'title':'Bikes'
	}
    return render(request,'blog/bikes.html', context)

class RowerSzczegoly(DetailView):
    model = Bike

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

class AkcesoriaSzczegoly(DetailView):
    model = Accesor

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