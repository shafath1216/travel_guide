from django.shortcuts import render, get_object_or_404
from .models import City
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def city_detail(request, id):
    city = get_object_or_404(City, pk=id)
    return render(request, 'city_detail.html', {'city': city})