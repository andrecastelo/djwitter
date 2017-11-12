from django.shortcuts import render

from core.models import Tweet

def index(request):
    data = {'tweets': Tweet.objects.order_by('-created_at').all()}

    return render(request, 'index.html', data)
