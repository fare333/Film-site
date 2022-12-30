from django.shortcuts import render,redirect
from .models import Film,Category
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from .forms import *
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    films = Film.objects.all()
    context = {'films': films}
    return render(request, 'base/index.html', context) 

@login_required(login_url='login')
def film_details(request,product_id):
    film = Film.objects.get(id=product_id)
    related_movies = Film.objects.filter(category=film.category).exclude(id=product_id)
    context = {'film': film,"related_movies":related_movies}
    return render(request, 'base/film_details.html', context)

def popular_films(request):
    films = Film.objects.filter(popular=True)
    context = {'films': films}
    return render(request, 'base/popular_films.html', context)

def trending_films(request):
    films = Film.objects.filter(trending=True)
    context = {'films': films}
    return render(request, 'base/trending_film.html', context)

def search(request):
    if request.method == "POST":
        search = request.POST.get("search")
        films = Film.objects.filter(title__icontains=search)
        context = {'films': films}
        return render(request, 'base/search.html', context)
    
def categories(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'base/categories.html', context)

def category_films(request,pk):
    category = Category.objects.get(id=pk)
    films = Film.objects.filter(category=category)
    context = {'films': films,"category":category}
    return render(request, 'base/category_films.html', context)
    

def signin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return redirect('login')
        
    return render(request, 'base/login/login.html')

def register(request):
    form = Register()
    if request.method == "POST":
        form = Register(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return redirect('register')
        
    context = {"form":form}
    return render(request, 'base/login/register.html', context)

def signout(request):
    logout(request)
    return redirect('home')

def all_categories(request):
    return {
        "categories":Category.objects.all()
    }