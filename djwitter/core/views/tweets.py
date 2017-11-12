from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from core.models import Tweet
from core.forms import TweetForm


@login_required(login_url='/login')
def tweet_view(request):
    form = TweetForm(request.POST)

    if not form.is_valid():
        messages.error(request, form.errors)
        return HttpResponseRedirect(reverse('index'))

    tweet_body = form.cleaned_data['message']
    Tweet.objects.create(user=request.user, body=tweet_body)
    messages.success(request, "Tweet posted")

    return HttpResponseRedirect(reverse('index'))
