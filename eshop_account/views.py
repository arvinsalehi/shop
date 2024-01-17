from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, models, logout
from .forms import Login, Register, User_edit


def Login_user(request):
    if request.user.is_authenticated:
        return redirect("Home")
    Login_form = Login(request.POST or None)
    if Login_form.is_valid():
        username = Login_form.cleaned_data.get("username")
        password = Login_form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            Login_form.add_error('username', "ایمیل یا رمز اشتباه است!")

    context = {
        "Login_form": Login_form,
    }
    return render(request, 'account/login.html', context)


def Register_user(request):
    if request.user.is_authenticated:
        return redirect("Home")
    Register_form = Register(request.POST or None)
    if Register_form.is_valid():
        first_name = Register_form.cleaned_data.get("first_name")
        last_name = Register_form.cleaned_data.get("last_name")
        username = Register_form.cleaned_data.get("username")
        email = Register_form.cleaned_data.get("email")
        password = Register_form.cleaned_data.get("password")
        models.User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email,
                                        password=password)
        return redirect("login_register:Login")

    context = {
        "Register_form": Register_form,
    }

    return render(request, 'account/register.html', context)


def log_out(request):
    logout(request)
    return redirect("login_register:Login")


@login_required(login_url="/log-out")
def user_panel(request):
    return render(request, "account/user_panel.html", {})


@login_required(login_url="/log-out")
def user_edit_panel(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    if user is None:
        raise Http404()
    edit_form = User_edit(request.POST or None,
                          initial={'first_name': request.user.first_name, 'last_name': request.user.last_name})

    if edit_form.is_valid():
        first_name = edit_form.cleaned_data.get('first_name')
        last_name = edit_form.cleaned_data.get('last_name')
        print(first_name)
        print(last_name)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

    context = {
        "edit_form": edit_form,
    }
    return render(request, "account/user_edit_panel.html", context)


@login_required(login_url="/log-out")
def user_sidebar(request):
    return render(request, "account/components/user_panel_partial.html", {})
