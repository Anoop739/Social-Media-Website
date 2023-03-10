from django.db import models
from django.contrib.auth.models import User


class Posts(models.Model):
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=50)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.post_name


class UserProfile(models.Model):
    is_active=models.BooleanField(default=True)
    profile_pic=models.ImageField(upload_to="images",null=True,blank=True)
    bio=models.CharField(max_length=100)
    timeline_pic=models.ImageField(upload_to="images",null=True,blank=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")

    def __str__(self):
        return self.bio
class Post(models.Model):
    description=models.CharField(max_length=200) 
    image=models.ImageField(upload_to="images",null=True,blank=True) 
    user=models.ForeignKey(User,on_delete=models.CASCADE) 
    created_date=models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self().description


class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="auther")
    Post=models.ForeignKey(Post,on_delete=models.CASCADE)
    created_date=models.DateField(auto_now_add=True)
    comment=models.CharField(max_length=200)