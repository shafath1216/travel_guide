from django.shortcuts import render, get_object_or_404,redirect
from .models import City,Review
from django.contrib.auth.decorators import login_required


# Create your views here.
def city_detail(request, id):
    city = get_object_or_404(City, pk=id)
    reviews = city.reviews.all().order_by('-created_at')

    if request.method == "POST":
        if request.user.is_authenticated:
            text = request.POST.get("text")
            if text:
                Review.objects.create(
                    city=city,
                    user=request.user,
                    text=text
                )
            return redirect('city_detail', id=city.pk)
        else:
            return redirect('login')

    return render(request, 'city_detail.html', {
        'city': city,
        'reviews': reviews
    })


from django.shortcuts import render
from .models import Package

def packages_list(request):
    packages = Package.objects.all().order_by('city__name')
    return render(request, 'packages.html', {'packages': packages})