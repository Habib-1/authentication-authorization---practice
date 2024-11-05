from django.urls import path
from .import views
urlpatterns = [
    path('',views.home, name='home'),
    path('register/',views.register,name='register'),
    path('log_in/',views.login, name='login'),
    path('logout/',views.logout,name="logout"),
    path('profile/',views.profile,name="profile"),
    path('change_password/',views.passChange,name="change_password"),
    path('change_password_withhout_old_password/',views.changePass,name="password2"),
]