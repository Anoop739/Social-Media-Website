from django.shortcuts import render,redirect
from web.forms import RegisterForm,LoginForm,ProfileForm,UserProfileForm,PostForm
from django.views.generic import View,CreateView,FormView,TemplateView,ListView,UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from api.models import UserProfile,Posts
from django.contrib import messages
from django.views.generic import View
from django.contrib.auth import authenticate,login,logout

class SignupView(View):
    def get(self,request,*args,**kwargs):
        form=RegisterForm()
        return render(request,"register.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("signin")
        else:
            return render(request,"register.html",{"form":form})
# class SignupView(CreateView):
#     model=User
#     form_class=RegisterForm
#     template_name="index.html"
#     success_url=reverse_lazy("signin")
class SigninView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"log.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            print(uname,pwd)
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                return redirect("index")                                
            else:
                return render(request,"login.html",{"form":form})
        else:
            return render(request,"login.html",{"form":form})
# class SignInView(FormView):
#     template_name="login.html"
#     form_class=LoginForm
#     def post(self,request,*args,**kwargs):
#         form=LoginForm(request.POST)
#         if form.is_valid():
#             uname=form.cleaned_data.get("username")
#             pwd=form.cleaned_data.get("password")
#             usr=authenticate(request,username=uname,password=pwd)
#             if usr:
#                 login(request,usr)
#                 return redirect("index")
#             else:
#                 return render(request,"login.html",{"form":self.form_class})
# class IndexView(View):
#     def get(self,request,*args,**kwargs):
#       return render(request,"index.html")

# class IndexView(View):
#     def get(self,request,*args,**kwargs):
#         form=ProfileForm()
#         return render(request,"index.html",{"form":form})
#     def post(self,request,*args,**kwargs):
#         form=ProfileForm(request.POST,files=request.FILES)
#         if form.is_valid():
#             usr=User.objects.get(username=request.user.username)
#             form.instance.user=usr
#             form.save()
#             return redirect("profile-detail")
#         else:
#             return render(request,"index.html",{"form":form})
        


class IndexView(CreateView,ListView):
     model=Posts
     form_class=PostForm

     template_name="index.html"
     success_url=reverse_lazy("index")
     context_object_name="posts"

     def form_valid(self, form):
         form.instance.user=self.request.user
         return super().form_valid(form) 
     
    

class ProfileView(View):
    def get(self,request,*args,**kwargs):
        qs=UserProfile.objects.filter(user=request.user)
        return render(request,"profile-detail.html",{"profile":qs})

class ProfileUpdateView(UpdateView):
    model=UserProfile
    form_class=UserProfileForm
    template_name="profile-edit.html"
    success_url=reverse_lazy("profile-detail")
    pk_url_kwarg="id"

class ProfileDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        ques=UserProfile.objects.get(id=id).delete()
        return redirect("index")
    
class SignoutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("signin")
    




        

        
        

