from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse_lazy
from website.forms import SignUpForm
from django.views.generic import CreateView


# Create your views here.
def home(request):
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
            {},
        )


def login_user(request):
    pass


def logout_user(request):
    logout(request)
    messages.success(request, "Logged Out....")
    return redirect("home")


class RegistrationView(CreateView):
    template_name = "registration.html"
    form_class = SignUpForm
    success_url = reverse_lazy("home")
