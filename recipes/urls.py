from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('update/', views.update, name="update"),
    path('add/', views.add, name="add"),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('update_profile/', views.update_profile, name='profile_update'),
    path('delete_recipe/<id>/', views.recipe_delete, name='recipe_delete'),
]