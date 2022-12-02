from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm 


# Create your views here.
def register(request):

    return render(request, 'register.html', {})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/views/')
    else:
        form = AuthenticationForm(request)
    form.fields['username'].widget.attrs['class'] = 'form-control'
    form.fields['username'].widget.attrs['placeholder'] = 'admin'
    form.fields['username'].label_classes = ('form-control',)

    form.fields['password'].widget.attrs['class'] = 'form-control'
    form.fields['password'].widget.attrs['placeholder'] = 'password'
    form.fields['password'].label_classes = 'form-control'
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
