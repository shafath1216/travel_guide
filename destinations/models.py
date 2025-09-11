from django.db import models
from django.contrib.auth.models import User


class City(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='city_images/')  # stored in media/city_images/
    google_map_embed = models.TextField(blank=True, null=True)  # store iframe embed URL

    def __str__(self):
        return self.name
    

class Attraction(models.Model):
    city = models.ForeignKey(City, related_name="attractions", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='attraction_images/')
    entry_fee = models.CharField(max_length=100, blank=True, null=True)  # e.g. "150 BDT" or "Free"

    def __str__(self):
        return f"{self.name} ({self.city.name})"


class Hotel(models.Model):
    city = models.ForeignKey('City', on_delete=models.CASCADE, related_name='hotels')
    name = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=300, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    website = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name or "Unnamed Hotel"


class Restaurant(models.Model):
    city = models.ForeignKey('City', on_delete=models.CASCADE, related_name='restaurants')
    name = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=300, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    website = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name or "Unnamed Restaurant"
    


class Review(models.Model):
    city = models.ForeignKey(City, related_name="reviews", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} on {self.city.name}"
    
class Package(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # e.g., 2500.00 BDT
    duration_days = models.IntegerField()  # number of days
    city = models.ForeignKey(City, related_name='packages', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.city.name})"    