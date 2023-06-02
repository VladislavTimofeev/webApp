from django.shortcuts import render

def index(request):
    data = {
        'title': 'Main page',
        'values': ['Some', 'Hello', '123']
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')

