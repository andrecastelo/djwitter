from django.shortcuts import render
from .models import Tweet

# Create your views here.
def index(request):
    data = {
        'tweets': Tweet.objects.all(),
    }

    return render(request, 'index.html', data)