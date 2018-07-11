from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views

# Blog accounts view created by CarlaPastor
app_name = 'accounts'

urlpatterns = [
    url(r"^", include("django.contrib.auth.urls")),
    url(r"login/$", views.Login.as_view(), name="login"),
    url(r"logout/$", auth_views.LogoutView.as_view(), name="logout"),
    url(r"signup/$", views.SignUp.as_view(), name="signup"),
]
