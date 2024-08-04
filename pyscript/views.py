from django.shortcuts import render
from django.http import JsonResponse
import time
import os

def index(request):
    return render(request, 'pyscript/index.html')
