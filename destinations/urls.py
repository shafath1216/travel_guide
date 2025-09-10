from django.urls import path
from . import views

urlpatterns = [
    path('cities/<int:id>/', views.city_detail, name='city_detail'),
]
