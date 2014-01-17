# encoding: utf-8

from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from profiles.forms import LoginForm
from profiles.models import UttrUser

def login_view(request):
    ctx = {}
    next_url = request.GET.get('next', False)
    if next_url:
        ctx['next_url'] = next_url
    login_form = LoginForm(initial={'next_url': next_url})
    ctx['login_form'] = login_form

    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        ctx['login_form'] = login_form
        if login_form.is_valid():
            email = login_form.cleaned_data['email']
            password = login_form.cleaned_data['password']

            user = authenticate(email=email, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    message = "Thank you for logging in"
                    messages.success(request, message)
                    next_url = request.POST.get('next_url')
                    if next_url != '':
                        return redirect(next_url)
                    else:
                        return redirect(reverse('profiles:home'))
                else:
                    messages.warning(request, "Thank you for logging in. Please change your password.")
                    return redirect(reverse('profiles:change_password'))
            else:
                message = "Sorry. There was an issue with your username/password"
                messages.error(request, message)
                return render(request, 'profiles/login.html', ctx)

    return render(request, 'profiles/login.html', ctx)

def index(request):
    ctx = {}
    ctx['home_active'] = True

    return render(request, 'profiles/index.html', ctx)

def logout_view(request):
    user = request.user

    logout(request)
    messages.success(request, "%s has successfuly logged out" % user.email)

    return redirect(reverse('home'))

def change_password(request):
    ctx = {}
    return render(request, 'profiles/change_password.html', ctx)