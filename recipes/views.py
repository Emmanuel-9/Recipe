from pyexpat.errors import messages
from django.http import request
from django.shortcuts import render, redirect
from recipes.models import Recipe,User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout as django_logout
from recipes.forms import RecipeForm,UpdateForm,ProfileForm

# Create your views here.
def index(request):
    recipe_list = Recipe.objects.order_by('-pub_date')
    context = {
        'recipe_list': recipe_list,
    }

    return render(request,'index.html', context)

def add(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = RecipeForm() 
    return render (request,'user/add_recipe.html',{"form": form})




def update(request):
    if request.method == 'POST':
        form = UpdateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UpdateForm() 
    return render (request,'user/update.html',{"form": form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            user = authenticate(username=username, password1=password1, password2=password2)
            login(request, user)
            messages.success(request, ("Registration Successful"))
            return redirect('/')
    else:
        form = UserCreationForm()

    return render (request,'registration/register.html',{"form": form})

def login_user(request):
    if  request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.success(request, ("Failed Authentication"))
            return redirect('login')    

    else:
        return render(request, 'registration/login.html',{})

def logout(request):
    django_logout(request)
    #messages.success(request, ("You were logged out"))
    return redirect('/')         


def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ProfileForm() 
    return render (request,'user/profile.html',{"form": form})    