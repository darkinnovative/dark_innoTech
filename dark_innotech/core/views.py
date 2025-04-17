from django.http import HttpResponse
from django.shortcuts import render  ,redirect

from django.contrib import messages


def index(request):
    return render(request, 'index.html')

def blog(request):
    return render(request, 'blog.html')

def blog_details(request):
    return render(request, 'blog-details.html')

def portfolio_details(request):
    return render(request, 'portfolio-details.html')

def service_details(request):
    return render(request, 'service-details.html')


def service_pages(request):
    return render(request, 'service-page.html')


