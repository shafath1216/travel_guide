from django.db import models


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