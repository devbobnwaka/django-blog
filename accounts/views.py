from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm 


def form_fields(field_name, form, placeholder):
    form.fields[field_name].widget.attrs['class'] = 'form-control'
    form.fields[field_name].widget.attrs['placeholder'] = placeholder
    form.fields[field_name].label_classes = ('form-control',)

# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect('/views/')
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('/views/')
    context = {
        "form":form
    }        

    form_fields('username', form, 'username')
    form_fields('password1', form, 'password')
    form_fields('password2', form, 'password confirmation')
    return render(request, 'register.html', context)

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/views/')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/views/')
    else:
        form = AuthenticationForm(request)
    form_fields('username', form, 'username')
    form_fields('password', form, 'password')
    context = {
        "form": form
    }
    return render(request, "login.html", context)

def logout_view(request):
    if not request.user.is_authenticated:
        return redirect("/login/")
    if request.method == "POST":
        logout(request)
        return redirect("/login/")
    return render(request, "logout.html", {})
