from django.urls import path
from . import views



urlpatterns = [
    path("",views.index,name="index"),
    path("sigup",views.signup_user,name="signup"),
    path("login",views.login_user,name="login"),
    path("logout",views.logout_user,name="logout"),
    path("edit",views.edit_user,name="edit"),
    path("change",views.changePassword,name="change"),




]
