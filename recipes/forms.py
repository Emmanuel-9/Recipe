#from distutils.command.upload import upload
from django import forms
from django.contrib.auth.forms import UserCreationForm
from recipes.models import Recipe,User
from django.db import transaction

class UpdateForm(forms.Form):
    title = forms.CharField(max_length=100)
    image = forms.ImageField()
    description = forms.CharField(max_length=100)
    algorithm = forms.CharField(widget=forms.Textarea)

    def __str__(self):
        return self.title


    def save_update(self, **kwargs):
        super().save()

    

    def del_update(self):
        self.delete()    

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('Title', 'Description', 'Instructions', 'pub_date')
    

class ProfileForm(forms.Form):
    name = forms.CharField()
    email = forms.CharField()
    recipes = forms.IntegerField()

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