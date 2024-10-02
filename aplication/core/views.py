from django.shortcuts import render

# Create your views here.
def home(request):
    data = {'title1':'Doctor', 'title2':'Centro medico'}
    return render(request, 'core/home.html', data)