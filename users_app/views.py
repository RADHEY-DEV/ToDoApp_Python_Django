from django.shortcuts import render, redirect
from .forms import CustomRegistrationForm
from django.contrib import messages


def register(request):
    if request.method=="POST":
        register_form = CustomRegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, ("New User Account Created, Login to get started"))
            return redirect('todolist')

    else:
        register_form = CustomRegistrationForm()
    return render(request, 'register.html', {'register_form':register_form} )