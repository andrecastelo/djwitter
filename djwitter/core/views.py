from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Tweet
from .forms import LoginForm, TweetForm


# Create your views here.
def index(request):
    data = {'tweets': Tweet.objects.order_by('-created_at').all()}

    return render(request, 'index.html', data)


def show_login(request):
    return render(request, 'login.html', {'form': LoginForm()})

def do_login(request):
    form = LoginForm(request.POST)

    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        print(username, password)
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            request.session['success'] = "You are now logged in."
            messages.success(request, 'You are now logged in.')
            return HttpResponseRedirect('/')

    messages.error(request, "The username and password were incorrect.")
    return HttpResponseRedirect(reverse('login'))


def login_view(request):
    if request.method == 'POST':
        return do_login(request)
    else:
        return show_login(request)

def logout_view(request):
    logout(request)
    messages.success(request, "You are logged out.")
    return HttpResponseRedirect(reverse('index'))


@login_required(login_url='/login')
def tweet_view(request):
    form = TweetForm(request.POST)

    if not form.is_valid():
        messages.error(request, form.errors)
        return HttpResponseRedirect(reverse('index'))

    tweet_body = form.cleaned_data['message']
    Tweet.objects.create(user=request.user, body=tweet_body)

    return HttpResponseRedirect(reverse('index'))
