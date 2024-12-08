from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm 
from django.contrib import messages
from django.utils.html import strip_tags
from shop.models import Order, Rating
from django.contrib.auth.decorators import login_required

def register(request):
    form = RegistrationForm() 
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid(): 
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home_page')  
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, strip_tags(error))      

    return render(request, 'register_page.html', {'form': form})


def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username') 
        password = request.POST.get('password')        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)   
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')   

    return render(request, 'login_page.html')


def landing_page(request):
    return render(request, 'landing_page.html')

@login_required(login_url='/login')
def home_page(request):
    return render(request, 'home_page.html')

@login_required(login_url='/login')
def profile(request): 
    user = request.user   
    orders = Order.objects.filter(user=user).order_by('-created_at')   
    ratings = Rating.objects.filter(user=user)   
    context = {
        'user': user,
        'orders': orders,
        'ratings': ratings,
    } 
    return render(request, 'profile.html', context)

def logout_user(request):
    logout(request)
    return redirect('landing_page')










 
# def login(request):
#     return render(request, 'login.html')

# def register(request):
#     return render(request, 'register.html')

# def blog1(request):
#     return render(request, 'blog1.html')

 

# def product_lavender_pebbles(request):
#     return render(request, 'product_lavender_pebbles.html')

 

# def quiz(request):
#     return render(request, 'quiz.html')

# def results(request):
#     return render(request, 'results.html')
