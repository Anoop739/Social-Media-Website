from django import forms
from django.contrib.auth.models import User
from api.models import UserProfile,Post
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

    class Meta:
        model=User
        fields={"first_name","last_name","email","username","password"}
        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "last_name":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "password":forms.PasswordInput(attrs={"class":"form-control"})
        }
class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

class ProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=["profile_pic","bio","timeline_pic"]

class UserProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=["profile_pic","bio","timeline_pic"]

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=["description","image"]
