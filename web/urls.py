from django.urls import path
from web import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path("register/",views.SignupView.as_view(),name="signup"),
    path("login/",views.SigninView.as_view(),name="signin"),
    path("home/",views.IndexView.as_view(),name="index"),
    path("profile",views.ProfileView.as_view(),name="profile-detail"),
    path("profile/<int:id>/change",views.ProfileUpdateView.as_view(),name="profile-update"),
    path("profile/<int:pk>/remove",views.ProfileDeleteView.as_view(),name="profile-delete"),
    path("logout",views.SignoutView.as_view(),name="signout")




]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
