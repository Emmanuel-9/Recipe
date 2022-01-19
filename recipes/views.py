#from django import template
#from django.http import request
#from django.shortcuts import render
from django.http import HttpResponse,request
from django.template import loader

from recipes.models import Recipe

# Create your views here.
def index(request):
    recipe_list = Recipe.objects.order_by('-pub_date')
    template = loader.get_template('index.html')
    context = {
        'recipe_list': recipe_list,
    }

    return HttpResponse(template.render(context, request))