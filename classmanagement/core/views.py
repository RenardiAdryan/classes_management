from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from core.models import *
from django.http import HttpResponse
# Create your views here.
def landing(request):
    return render(request, 'landing.html')

def login_view(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('core:home')
        
        return render(request, 'login.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_auth = authenticate(request=request, email=email, password=password)
        if user_auth:
            login(request, user_auth)
        return redirect('core:home')
    
def logout_view(request):
    logout(request)
    return redirect('core:landing')

#AUTHENTTICATION NEEDED
@login_required
def home(request):
    if request.method == 'GET':
        classes = Classes.objects.filter().order_by("created_at")
        teachers = User.objects.filter(teacher__isnull=False)
        context={
            "classes": classes,
            "teachers": teachers
        }
        return render(request, 'core/home.html',context)
    else:

        if 'create-classes' in request.POST:

            name = request.POST.get('name',None)
            teacher_assignee = request.POST.get('assignee',None)
   
            user = User.objects.get(id=teacher_assignee)

            Classes.objects.create(
                name = name,
                teacher = user.teacher
            )

        return redirect('core:home') 

def class_detail(request,id):
    classes = Classes.objects.get(id=id)
    context={
        "classes": classes
    }
    return render(request, 'core/class-detail.html',context)