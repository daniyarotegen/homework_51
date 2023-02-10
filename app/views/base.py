from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render


def index_view(request: WSGIRequest):
    cat_name = request.GET.get('cat_name')
    return render(request, 'index.html', context={
        'cat_name': cat_name
    })