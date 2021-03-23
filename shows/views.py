from django.shortcuts import render

def home(request):
	return render(request, 'shows/home.html')


def about(request):
    return render(request, 'shows/about.html', {'title': 'About'})
