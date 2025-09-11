from django.urls import path
from .views import home,login_view,signup_view,cities,logout_view

urlpatterns=[

path('',cities,name='cities'),
path('login/',login_view,name='login'),
path('signup/',signup_view,name='signup'),
path('logout/',logout_view,name='logout'),

]