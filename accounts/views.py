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
from django.contrib import messages

def login_view(request):
    # If 'next' exists in GET, show message
    if request.GET.get('next'):
        messages.info(request, 'You need to log in to view the page you requested.')

    if request.method == 'POST':
        # your existing login logic
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('cities')  # default redirect
        else:
            messages.error(request, 'Invalid credentials')

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
    return redirect('cities')
