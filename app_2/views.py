from django.shortcuts import render,redirect
from .forms import registerForm
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
# Create your views here.
def home(request):
    
    return render(request,'home.html')

def register(request):
    if request.method=="POST":
        form=registerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
      
    form=registerForm()
    return render(request,'signUp.html',{'form':form})

def login(request):
    
    if request.method=="POST":
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=auth.authenticate(username=username, password=password)
            if user is not None:
               auth.login(request, user)
               return redirect('profile')
            else:
                return redirect('login')
    form=AuthenticationForm()
    return render(request,'login.html',{'form':form})


def logout(request):
    auth.logout(request)
    return redirect('login')

def profile(request):
    if request.user.is_authenticated :
         return render(request,'profile.html')
    else:
        return redirect('login')
    
def passChange(request):
    if request.method=="POST":
        form=PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            form.save()
            auth.update_session_auth_hash(request,form.user)
            return redirect('profile')
        else:
           return redirect('change_password')
        
    else:
        form=PasswordChangeForm(request)

    return render(request,'passwordChange.html',{'form':form})

def changePass(request):
    if request.method=="POST":
        form=SetPasswordForm(request.user,request.POST)
        if form.is_valid():
            form.save()
            auth.update_session_auth_hash(request,form.user)
            return redirect('profile')
        else:
           return redirect('change_password')
        
    else:
        form=SetPasswordForm(request)

    return render(request,'pasword2.html',{'form':form})
