from django.shortcuts import render, get_object_or_404,redirect
from .models import City,Review
from django.contrib.auth.decorators import login_required


# Create your views here.
from django.shortcuts import get_object_or_404, redirect, render
from .models import City, Review
from django.contrib.auth.models import User

def city_detail(request, id):
    city = get_object_or_404(City, pk=id)
    reviews = city.reviews.all().order_by('-created_at')

    if request.method == "POST":
        text = request.POST.get("text")
        if text:
            # Use the logged-in user, or a default Guest user if not logged in
            if request.user.is_authenticated:
                user = request.user
            else:
                # Get or create a "Guest" user
                user, created = User.objects.get_or_create(username='Guest', defaults={'email': 'guest@example.com'})
            
            Review.objects.create(
                city=city,
                user=user,
                text=text
            )
        return redirect('city_detail', id=city.pk)

    return render(request, 'city_detail.html', {
        'city': city,
        'reviews': reviews
    })



from django.shortcuts import render
from .models import Package
@login_required(login_url='login')
def packages_list(request):
    packages = Package.objects.all().order_by('city__name')
    return render(request, 'packages.html', {'packages': packages})