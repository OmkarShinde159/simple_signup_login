from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


# Create your views here.
# create a views for signup and save the user

@login_required             # used to protect the view
def home(request):
    return render(request=request, template_name="home.html", context={})

def auth_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("base:login")
    else:
        form = UserCreationForm()
    return render(request=request, template_name="registration/signup.html", context={"form": form})

def custom_logout(request):
    logout(request)
    return redirect('base:login')


