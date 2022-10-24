from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

@require_http_methods(['GET', 'POST'])
def index(request):
    data = {"header": "Hello World", "message": "Welcome to project"}
    return render(request, 'index.html', context=data)