from django.shortcuts import render


def landing_page(request):
    return render(request, 'landing/landing.html')

def about_page(request):
    return render(request, 'landing/about.html')
