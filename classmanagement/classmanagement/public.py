from core.models import *
from django.shortcuts import get_object_or_404, redirect, render

def home(request):
    print("MASUK LANDINGGGGggggggg")
    return render(request, 'landing.html')