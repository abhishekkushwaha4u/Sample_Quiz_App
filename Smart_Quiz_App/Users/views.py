from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
def home(request):
    return render(request,"Users/home.html")

def signup(request):
    if request.method=="POST":
        newUser = UserCreationForm(request.POST)
        if newUser.is_valid():
            user = newUser.save()
            username = newUser.cleaned_data.get('username')
            messages.success(request,f"Account created for : {username}")
            login(request,user)
            messages.success(request, f"You have logged in as : {username}")
            return redirect("Users:homepage")
        else:
            for message in newUser.error_messages:
                messages.error(request,f"{message}:{newUser.error_messages[message]}")
    newUser = UserCreationForm
    return render(request,"Users/signup.html",{"newUser":newUser})


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request,template_name="Users/login.html",context={"form": form})

def logout_request(request):
    logout(request)
    messages.info(request,"Logged out successfully !")
    return render(request,"Users/logout.html")





