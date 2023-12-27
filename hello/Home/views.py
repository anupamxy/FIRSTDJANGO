from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Contact
from django.utils import timezone  # For getting the current date and time

def index(request):
    if request.user.is_anonymous:
        return redirect('login')
    else:
        return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=timezone.now())
        contact.save()

    return render(request, 'contact.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            # Handle invalid login credentials here
            # You might want to render the login page again with an error message
            return render(request, 'login.html', {'error_message': 'Invalid credentials'})

    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('login')



# Create your views here.
