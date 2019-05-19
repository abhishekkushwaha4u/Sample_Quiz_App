from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
def home(request):
    return render(request,"Users/home.html")

def signup(request):
    if request.method=="POST":
        newUser = UserCreationForm(request.POST)
        if newUser.is_valid():
            user = newUser.save()
            user.is_staff = True
            login(request,user)
            return redirect("Users:homepage")
        else:
            for message in newUser.error_messages:
                print(newUser.error_messages[message])
    newUser = UserCreationForm
    return render(request,"Users/signup.html",{"newUser":newUser})

