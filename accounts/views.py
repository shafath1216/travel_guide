from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from destinations.models import City


# ----------------------
# Home view
# ----------------------
def home(request):
    return render(request, 'home.html')

# ----------------------
# Cities view (login required)
# ----------------------
@login_required
def cities(request):
    query = request.GET.get('q')  # Get search term from URL query parameter
    if query:
        # Filter cities by name containing the search term (case-insensitive)
        cities_list = City.objects.filter(name__icontains=query)
    else:
        # If no search term, show all cities
        cities_list = City.objects.all()
    
    return render(request, 'cities.html', {
        "cities": cities_list,
        "query": query  # Pass the query back to template to keep it in the input box
    })
# Login view
# ----------------------
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        user = authenticate(request, username=username, password=password)
        if user:
            auth_login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('cities')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

# ----------------------
# Signup view
# ----------------------
def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()
        confirm_password = request.POST.get('confirm_password', '').strip()

        # Validations
        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already registered.')
        else:
            # Create user and hash password automatically
            user = User.objects.create_user(username=username, email=email, password=password)
            auth_login(request, user)  # Auto-login after signup
            messages.success(request, f'Account created successfully. Welcome, {user.username}!')
            return redirect('cities')

    return render(request, 'signup.html')

# ----------------------
# Logout view
# ----------------------
def logout_view(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('home')
