from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, get_user_model, login, logout

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def login_view(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            print("Already Authenticated Successfully")
            return redirect('core:home')
        
        return render(request, 'login.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_auth = authenticate(request=request, email=email, password=password)
        if user_auth:
            login(request, user_auth)
            print("Login Successfully")

        return redirect('core:home')