from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse_lazy
from website.forms import SignUpForm
from .models import Ottplatform, Record


# Create your views here.
def home(request):
    records = Record.objects.all()
    # check to see if logging in
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        # authenticate
        user = authenticate(
            request,
            username=username,
            password=password,
        )
        if user is not None:
            login(request, user)
            messages.success(request, "You have been Logged In!")
            return redirect("home")
        else:
            messages.warning(
                request, "There was an Error Logging In. Please Try Again ....."
            )
            return redirect("home")
    else:
        return render(
            request,
            "home.html",
            {"records": records},
        )


def login_user(request):
    pass


def logout_user(request):
    logout(request)
    messages.success(request, "Logged Out....")
    return redirect("home")


def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            # Authenticate and Logged in
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "New User is Created and Logged In.........")
            return redirect("home")

    else:
        form = SignUpForm()
        return render(
            request,
            "registration.html",
            {"form": form},
        )
    return render(
        request,
        "registration.html",
        {"form": form},
    )
