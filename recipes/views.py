#from turtle import title
from django.contrib import messages
from django.http import request
from django.shortcuts import render, redirect,get_object_or_404
from recipes.models import Recipe,Profile,User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout as django_logout
from recipes.forms import RecipeForm,UpdateForm,ProfileForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    recipe_list = Recipe.objects.order_by('-pub_date')
    context = {
        'recipe_list': recipe_list,
    }

    return render(request,'index.html', context)


@login_required(login_url='login')
def add(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = RecipeForm() 
    return render(request,'user/add_recipe.html',{"form": form})



@login_required(login_url='login')
def update(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        form = UpdateForm(request.POST, request.FILES, instance=request.user.id)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UpdateForm(request.POST, request.FILES, instance=request.user.id) 
    return render(request,'user/update.html',{"form": form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            user = authenticate(username=username, password1=password1, password2=password2)
            #login(request, user)
            messages.success(request, "Registration Successful")
            return redirect('login')
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
    messages.success(request, ("You were logged out"))
    return redirect('/')         


def profile(request):
    profile_list = Profile.objects.all()
    context = {
        'profile_list': profile_list,
    }

    return render(request,'user/profile.html', context)

 
@login_required(login_url='login')
def update_profile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('profile', user.id)
    else:
        form = ProfileForm(request.POST,request.FILES, instance=request.user.userprofile) 
    return render(request,'user/update_profile.html',{"form": form})  


@login_required(login_url='login')
def recipe_delete(request, id):
    recipe_be_deleted = get_object_or_404(Recipe, id=id)
    if request.method == 'POST':
        recipe_be_deleted.delete() 
        return redirect('/')   