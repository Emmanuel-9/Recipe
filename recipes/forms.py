#from distutils.command.upload import upload
from email.policy import default
from django import forms
from django.contrib.auth.forms import UserCreationForm
from recipes.models import Recipe,User
from django.db import transaction

class UpdateForm(forms.Form):
    class Meta:
        model = Recipe
        fields = ('Title', 'Image', 'Description', 'Instructions')
    

    def __str__(self):
        return self.title


    def save_update(self):
        self.save()

    

    def del_update(self):
        self.delete()    

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('Title', 'Image', 'Description', 'Instructions')
    

class ProfileForm(forms.Form):
    name = forms.CharField(max_length=50)
    image = forms.ImageField()
    email = forms.EmailField()
    recipe_count = forms.IntegerField()

    def __str__(self):
        return self.name

    def save_profile(self):
        self.save()

    def del_profile(self):
        self.delete()    

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField()
    contact = forms.IntegerField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        user = User.objects.create(user=user)
        user.save()
        return user