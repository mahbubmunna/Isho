
from django.urls import path
from .views import items

urlpatterns = [
    path('home/', items, name='home'),
]
